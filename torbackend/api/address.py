from models import session
from common.libs.helper import getCurrentDate
from models.member import MemberAddress
from tornado.web import RequestHandler
from views.auth import ApiAuth

class WxAddressIndexHandler(ApiAuth,RequestHandler):
    def get(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        member_info = self.member_info
        list = session.query(MemberAddress).filter_by(status=1, member_id=member_info.id) \
            .order_by(MemberAddress.id.desc()).all()
        data_list = []
        if list:
            for item in list:
                tmp_data = {
                    "id": item.id,
                    "nickname": item.nickname,
                    "mobile": item.mobile,
                    "is_default": item.is_default,
                    "address": "%s%s%s%s" % (item.province_str, item.city_str, item.area_str, item.address),
                }
                data_list.append(tmp_data)
        resp['data']['list'] = data_list
        self.finish(resp)

class WxAddressSetHandler(ApiAuth,RequestHandler):
    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        id = int(self.get_argument('id',0))
        nickname = self.get_argument('nickname','')
        address = self.get_argument('address','')
        mobile = self.get_argument('mobile','')

        province_id = int(self.get_argument('province_id',0))
        province_str = self.get_argument('province_str','')
        city_id = int(self.get_argument('city_id',0))
        city_str = self.get_argument('city_str','')
        district_id = int(0 if not self.get_argument('district_id',0) else self.get_argument('district_id',0))
        district_str = self.get_argument('district_str','')

        member_info = self.member_info

        if not nickname:
            resp['code'] = -1
            resp['msg'] = "请填写联系人姓名~~"
            self.finish(resp)
            return

        if not mobile:
            resp['code'] = -1
            resp['msg'] = "请填写手机号码~~"
            self.finish(resp)
            return

        if province_id < 1:
            resp['code'] = -1
            resp['msg'] = "请选择地区~~"
            self.finish(resp)
            return

        if city_id < 1:
            resp['code'] = -1
            resp['msg'] = "请选择地区~~"
            self.finish(resp)
            return

        if district_id < 1:
            district_str = ''

        if not address:
            resp['code'] = -1
            resp['msg'] = "请填写详细地址~~"
            self.finish(resp)
            return

        if not member_info:
            resp['code'] = -1
            resp['msg'] = "系统繁忙，请稍后再试~~"
            self.finish(resp)
            return

        address_info = session.query(MemberAddress).filter_by(id=id, member_id=member_info.id).first()
        if address_info:
            model_address = address_info
        else:
            default_address_count = session.query(MemberAddress).filter_by(is_default=1, member_id=member_info.id,
                                                                  status=1).count()
            model_address = MemberAddress()
            model_address.member_id = member_info.id
            model_address.is_default = 1 if default_address_count == 0 else 0
            model_address.created_time = getCurrentDate()

        model_address.nickname = nickname
        model_address.mobile = mobile
        model_address.address = address
        model_address.province_id = province_id
        model_address.province_str = province_str
        model_address.city_id = city_id
        model_address.city_str = city_str
        model_address.area_id = district_id
        model_address.area_str = district_str
        model_address.updated_time = getCurrentDate()
        session.add(model_address)
        session.commit()
        self.finish(resp)

class WxAddressInfoHandler(ApiAuth,RequestHandler):
    def get(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        id = int(self.get_argument('id',0))
        member_info = self.member_info

        if id < 1 or not member_info:
            resp['code'] = -1
            resp['msg'] = "系统繁忙，请稍后再试~~"
            self.finish(resp)
            return

        address_info = session.query(MemberAddress).filter_by(id=id).first()
        if not address_info:
            resp['code'] = -1
            resp['msg'] = "系统繁忙，请稍后再试~~"
            self.finish(resp)
            return

        resp['data']['info'] = {
            "nickname": address_info.nickname,
            "mobile": address_info.mobile,
            "address": address_info.address,
            "province_id": address_info.province_id,
            "province_str": address_info.province_str,
            "city_id": address_info.city_id,
            "city_str": address_info.city_str,
            "area_id": address_info.area_id,
            "area_str": address_info.area_str
        }
        self.finish(resp)

class WxAddressOptHandler(ApiAuth,RequestHandler):
    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        id = int(self.get_argument('id',0))
        act = self.get_argument('act','')
        member_info = self.member_info

        if id < 1 or not member_info:
            resp['code'] = -1
            resp['msg'] = "系统繁忙，请稍后再试~~"
            self.finish(resp)
            return

        address_info = session.query(MemberAddress).filter_by(id=id, member_id=member_info.id).first()
        if not address_info:
            resp['code'] = -1
            resp['msg'] = "系统繁忙，请稍后再试~~"
            self.finish(resp)
            return

        if act == "del":
            address_info.status = 0
            address_info.updated_time = getCurrentDate()
            session.add(address_info)
            session.commit()
        elif act == "default":
            session.query(MemberAddress).filter_by(member_id=member_info.id) \
                .update({'is_default': 0})
            address_info.is_default = 1
            address_info.updated_time = getCurrentDate()
            session.add(address_info)
            session.commit()
        self.finish(resp)





