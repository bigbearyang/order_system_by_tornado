from models.member import Member
from models.food import Food
from models.pay import PayOrder
from models.pay import PayOrderItem
from models import session
from common.libs.urlmanager import UrlManager
from common.libs.helper import selectFilterObj,getDictListFilterField,getDictFilterField,getCurrentDate
from sqlalchemy import func
import json
from tornado.web import RequestHandler
from config import PAY_STATUS_MAPPING
from views.auth import Auth

class FinanceIndexHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        status = self.get_argument('status',None)
        if status:
            query = session.query(PayOrder).filter_by(status = int(status))
        else:
            query = session.query(PayOrder)
        pay_list = query.order_by(PayOrder.id.desc()).all()
        data_list = []
        if pay_list:
            pay_order_ids = selectFilterObj(pay_list, "id")
            pay_order_items_map = getDictListFilterField(PayOrderItem, PayOrderItem.pay_order_id, "pay_order_id",
                                                         pay_order_ids)

            food_mapping = {}
            if pay_order_items_map:
                food_ids = []
                for item in pay_order_items_map:
                    tmp_food_ids = selectFilterObj(pay_order_items_map[item], "food_id")
                    tmp_food_ids = {}.fromkeys(tmp_food_ids).keys()
                    food_ids = food_ids + list(tmp_food_ids)

                # food_ids里面会有重复的，要去重
                food_mapping = getDictFilterField(Food, Food.id, "id", food_ids)

            for item in pay_list:
                tmp_data = {
                    "id": item.id,
                    "status_desc": item.status_desc,
                    "order_number": item.order_number,
                    "price": item.total_price,
                    "pay_time": item.pay_time,
                    "created_time": item.created_time.strftime("%Y%m%d%H%M%S")
                }
                tmp_foods = []
                tmp_order_items = pay_order_items_map[item.id]
                for tmp_order_item in tmp_order_items:
                    tmp_food_info = food_mapping[tmp_order_item.food_id]
                    tmp_foods.append({
                        'name': tmp_food_info.name,
                        'quantity': tmp_order_item.quantity
                    })

                tmp_data['foods'] = tmp_foods
                data_list.append(tmp_data)

        resp_data['list'] = data_list
        resp_data['pay_status_mapping'] = PAY_STATUS_MAPPING
        resp_data['search_con'] = status
        resp_data['current'] = 'index'

        self.render("finance/index.html",**resp_data)


class FinancePayInfoHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        id = int(self.get_argument('id',0))
        reback_url = UrlManager.buildUrl("/finance/index")

        if id < 1:
            self.redirect(reback_url)

        pay_order_info = session.query(PayOrder).filter_by(id=id).first()
        if not pay_order_info:
            self.redirect(reback_url)

        member_info = session.query(Member).filter_by(id=pay_order_info.member_id).first()
        if not member_info:
            self.redirect(reback_url)

        order_item_list = session.query(PayOrderItem).filter_by(pay_order_id=pay_order_info.id).all()
        data_order_item_list = []
        if order_item_list:
            food_map = getDictFilterField(Food, Food.id, "id", selectFilterObj(order_item_list, "food_id"))
            for item in order_item_list:
                tmp_food_info = food_map[item.food_id]
                tmp_data = {
                    "quantity": item.quantity,
                    "price": item.price,
                    "name": tmp_food_info.name
                }
                data_order_item_list.append(tmp_data)

        address_info = {}
        if pay_order_info.express_info:
            address_info = json.loads(pay_order_info.express_info)

        resp_data['pay_order_info'] = pay_order_info
        resp_data['pay_order_items'] = data_order_item_list
        resp_data['member_info'] = member_info
        resp_data['address_info'] = address_info
        resp_data['current'] = 'index'
        self.render("finance/pay_info.html", **resp_data)

class FinanceAccountHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        query = session.query(PayOrder).filter_by(status=1)
        list = query.order_by(PayOrder.id.desc()).all()
        stat_info = session.query(PayOrder, func.sum(PayOrder.total_price).label("total")) \
            .filter(PayOrder.status == 1).first()
        resp_data['list'] = list
        resp_data['total_money'] = stat_info[1] if stat_info[1] else 0.00
        resp_data['current'] = 'account'
        self.render("finance/account.html", **resp_data)

class FinanceOderOpsHandler(Auth,RequestHandler):
    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        id = self.get_argument('id',0)
        act = self.get_argument('act','')
        pay_order_info = session.query(PayOrder).filter_by(id=id).first()
        if not pay_order_info:
            resp['code'] = -1
            resp['msg'] = "系统繁忙。请稍后再试~~"
            self.finish(resp)
            return

        if act == "express":
            pay_order_info.express_status = -6
            pay_order_info.updated_time = getCurrentDate()
            session.add(pay_order_info)
            session.commit()

        self.finish(resp)

