from models.food import Food
from models.member import MemberCart
from common.libs.member.cartservice import CartService
from common.libs.helper import selectFilterObj,getDictFilterField
from common.libs.urlmanager import UrlManager
from models import session
from views.auth import ApiAuth
import json
from tornado.web import RequestHandler

class WxCartIndexHandler(ApiAuth,RequestHandler):
    def get(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '添加购物车成功~', 'data': {}}
        member_info = self.member_info
        if not member_info:
            resp['code'] = -1
            resp['msg'] = "获取失败，伪登录~~"
            self.write(resp)
            return
        cart_list = session.query(MemberCart).filter_by(member_id=member_info.id).all()
        data_cart_list = []
        if cart_list:
            food_ids = selectFilterObj(cart_list, "food_id")
            food_map = getDictFilterField(Food, Food.id, "id", food_ids)
            for item in cart_list:
                tmp_food_info = food_map[item.food_id]
                tmp_data = {
                    "id": item.id,
                    "number": item.quantity,
                    "food_id": item.food_id,
                    "name": tmp_food_info.name,
                    "price": str(tmp_food_info.price),
                    "pic_url": UrlManager.buildImageUrl(tmp_food_info.main_image),
                    "active": True
                }
                data_cart_list.append(tmp_data)

        resp['data']['list'] = data_cart_list
        self.finish(resp)

class WxCartSetHandler(ApiAuth,RequestHandler):
    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '添加购物车成功~', 'data': {}}
        food_id = int(self.get_argument('id',0))
        number = int(self.get_argument('number',0))
        if food_id < 1 or number < 1:
            resp['code'] = -1
            resp['msg'] = "添加购物车失败-1~~"
            self.write(resp)
            return

        member_info = self.member_info
        if not member_info:
            resp['code'] = -1
            resp['msg'] = "添加购物车失败-2~~"
            self.write(resp)
            return

        food_info = session.query(Food).filter_by(id=food_id).first()
        if not food_info:
            resp['code'] = -1
            resp['msg'] = "添加购物车失败-3~~"
            self.write(resp)
            return

        if food_info.stock < number:
            resp['code'] = -1
            resp['msg'] = "添加购物车失败,库存不足~~"
            self.write(resp)
            return

        ret = CartService.setItems(member_id=member_info.id, food_id=food_info.id, number=number)
        if not ret:
            resp['code'] = -1
            resp['msg'] = "添加购物车失败-4~~"
            self.write(resp)
            return
        self.finish(resp)

class WxCartDelHandler(ApiAuth,RequestHandler):
    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '添加购物车成功~', 'data': {}}
        params_goods = self.get_argument('goods',None)

        items = []
        if params_goods:
            items = json.loads(params_goods)
        if not items or len(items) < 1:
            self.write(resp)
            return

        member_info = self.member_info
        if not member_info:
            resp['code'] = -1
            resp['msg'] = "删除购物车失败-1~~"
            self.write(resp)
            return

        ret = CartService.deleteItem(member_id=member_info.id, items=items)
        if not ret:
            resp['code'] = -1
            resp['msg'] = "删除购物车失败-2~~"
            self.write(resp)
            return
        self.finish(resp)
