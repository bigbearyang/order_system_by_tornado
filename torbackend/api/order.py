from tornado.web import RequestHandler
import json, decimal
from models.food import Food
from models.pay import PayOrder
from common.libs.urlmanager import UrlManager
from common.libs.helper import getCurrentDate
from common.libs.pay.payservice import PayService
from common.libs.member.cartservice import CartService
from models.member import MemberAddress
from models.member import OauthMemberBind
from views.auth import ApiAuth
from models import session

class WxOrderInfoHandler(ApiAuth,RequestHandler):
    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        params_goods = self.get_argument('goods',None)
        member_info = self.member_info
        params_goods_list = []
        if params_goods:
            params_goods_list = json.loads(params_goods)

        food_dic = {}
        for item in params_goods_list:
            food_dic[item['id']] = item['number']

        food_ids = food_dic.keys()
        food_list = session.query(Food).filter(Food.id.in_(food_ids)).all()
        data_food_list = []
        yun_price = pay_price = decimal.Decimal(0.00)
        if food_list:
            for item in food_list:
                tmp_data = {
                    "id": item.id,
                    "name": item.name,
                    "price": str(item.price),
                    'pic_url': UrlManager.buildImageUrl(item.main_image),
                    'number': food_dic[item.id]
                }
                pay_price = pay_price + item.price * int(food_dic[item.id])
                data_food_list.append(tmp_data)

        # 获取地址
        address_info = session.query(MemberAddress).filter_by(is_default=1, member_id=member_info.id, status=1).first()
        default_address = ''
        if address_info:
            default_address = {
                "id": address_info.id,
                "name": address_info.nickname,
                "mobile": address_info.mobile,
                "address": "%s%s%s%s" % (
                address_info.province_str, address_info.city_str, address_info.area_str, address_info.address)
            }

        resp['data']['food_list'] = data_food_list
        resp['data']['pay_price'] = str(pay_price)
        resp['data']['yun_price'] = str(yun_price)
        resp['data']['total_price'] = str(pay_price + yun_price)
        resp['data']['default_address'] = default_address
        self.finish(resp)

class WxOrderCreateHandler(ApiAuth,RequestHandler):
    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        type = self.get_argument('type','')
        note = self.get_argument('note','')
        express_address_id = int(self.get_argument('express_address_id'),0)
        params_goods = self.get_argument('goods',None)

        items = []
        if params_goods:
            items = json.loads(params_goods)

        if len(items) < 1:
            resp['code'] = -1
            resp['msg'] = "下单失败：没有选择商品~~"
            self.write(resp)
            return

        address_info = session.query(MemberAddress).filter_by(id=express_address_id).first()
        if not address_info or not address_info.status:
            resp['code'] = -1
            resp['msg'] = "下单失败：快递地址不对~~"
            self.write(resp)
            return

        member_info = self.member_info
        target = PayService()
        params = {
            "note": note,
            'express_address_id': address_info.id,
            'express_info': {
                'mobile': address_info.mobile,
                'nickname': address_info.nickname,
                "address": "%s%s%s%s" % (
                address_info.province_str, address_info.city_str, address_info.area_str, address_info.address)
            }
        }
        resp = target.createOrder(member_info.id, items, params)
        # 如果是来源购物车的，下单成功将下单的商品去掉
        if resp['code'] == 200 and type == "cart":
            CartService.deleteItem(member_info.id, items)
        self.finish(resp)

class WxOrderPayHandler(ApiAuth,RequestHandler):
    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        member_info = self.member_info
        order_sn = self.get_argument('order_sn','')
        pay_order_info = session.query(PayOrder).filter_by(order_sn=order_sn, member_id=member_info.id).first()
        if not pay_order_info:
            resp['code'] = -1
            resp['msg'] = "系统繁忙。请稍后再试~~"
            self.write(resp)
            return

        oauth_bind_info = session.query(OauthMemberBind).filter_by(member_id=member_info.id).first()
        if not oauth_bind_info:
            resp['code'] = -1
            resp['msg'] = "系统繁忙。请稍后再试~~"
            self.write(resp)
            return
        target_pay = PayService()
        target_pay.orderSuccess(pay_order_id = pay_order_info.id)
        self.write(resp)


class WxOrderOpsHandler(ApiAuth,RequestHandler):
    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        member_info = self.member_info
        order_sn = self.get_argument('order_sn','')
        act = self.get_argument('act','')
        pay_order_info = session.query(PayOrder).filter_by(order_sn=order_sn, member_id=member_info.id).first()
        if not pay_order_info:
            resp['code'] = -1
            resp['msg'] = "系统繁忙。请稍后再试~~"
            self.write(resp)
            return

        if act == "cancel":
            target_pay = PayService()
            ret = target_pay.closeOrder(pay_order_id=pay_order_info.id)
            if not ret:
                resp['code'] = -1
                resp['msg'] = "系统繁忙。请稍后再试~~"
                self.write(resp)
                return
        elif act == "confirm":
            pay_order_info.express_status = 1
            pay_order_info.updated_time = getCurrentDate()
            session.add(pay_order_info)
            session.commit()

        self.write(resp)



