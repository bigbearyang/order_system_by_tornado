from tornado.web import RequestHandler
from models.food import Food,FoodCat
from models import session
from common.libs.urlmanager import UrlManager
from models.member import MemberCart,MemberComments,Member
from common.libs.helper import getCurrentDate,getDictFilterField,selectFilterObj
from sqlalchemy import  or_
from views.auth import ApiAuth

class WxFoodIndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        cat_list = session.query(FoodCat).filter_by(status=1).order_by(FoodCat.weight.desc()).all()
        data_cat_list = []
        data_cat_list.append({
            'id': 0,
            'name': "全部"
        })
        if cat_list:
            for item in cat_list:
                tmp_data = {
                    'id': item.id,
                    'name': item.name
                }
                data_cat_list.append(tmp_data)
        resp['data']['cat_list'] = data_cat_list
        food_list = session.query(Food).filter_by(status=1) \
            .order_by(Food.total_count.desc(), Food.id.desc()).limit(3).all()

        data_food_list = []
        if food_list:
            for item in food_list:
                tmp_data = {
                    'id': item.id,
                    'pic_url': UrlManager.buildImageUrl(item.main_image)
                }
                data_food_list.append(tmp_data)

        resp['data']['banner_list'] = data_food_list
        self.finish(resp)

class WxFoodSearchHandler(RequestHandler):
    def get(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        cat_id = int(self.get_argument('cat_id',0))
        mix_kw = str(self.get_argument('mix_kw',''))
        p = int(self.get_argument('p',1))
        if p < 1:
            p = 1

        page_size = 10
        offset = (p - 1) * page_size
        query = session.query(Food).filter_by(status=1)
        if cat_id > 0:
            query = query.filter_by(cat_id=cat_id)

        if mix_kw:
            rule = or_(Food.name.ilike("%{0}%".format(mix_kw)), Food.tags.ilike("%{0}%".format(mix_kw)))
            query = query.filter(rule)

        food_list = query.order_by(Food.total_count.desc(), Food.id.desc()) \
            .offset(offset).limit(page_size).all()

        data_food_list = []
        if food_list:
            for item in food_list:
                tmp_data = {
                    'id': item.id,
                    'name': "%s" % (item.name),
                    'price': str(item.price),
                    'min_price': str(item.price),
                    'pic_url': UrlManager.buildImageUrl(item.main_image)
                }
                data_food_list.append(tmp_data)
        resp['data']['list'] = data_food_list
        resp['data']['has_more'] = 0 if len(data_food_list) < page_size else 1
        self.finish(resp)

class WxFoodInfoHandler(ApiAuth,RequestHandler):
    def get(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        id = int(self.get_argument('id',0))
        food_info = session.query(Food).filter_by(id=id).first()
        if not food_info or not food_info.status:
            resp['code'] = -1
            resp['msg'] = "美食已下架"
            self.write(resp)
            return

        member_info = self.member_info
        cart_number = 0
        if member_info:
            cart_number = session.query(MemberCart).filter_by(member_id=member_info.id).count()
        resp['data']['info'] = {
            "id": food_info.id,
            "name": food_info.name,
            "summary": food_info.summary,
            "total_count": food_info.total_count,
            "comment_count": food_info.comment_count,
            'main_image': UrlManager.buildImageUrl(food_info.main_image),
            "price": str(food_info.price),
            "stock": food_info.stock,
            "pics": [UrlManager.buildImageUrl(food_info.main_image)]
        }
        resp['data']['cart_number'] = cart_number
        self.finish(resp)

class WxFoodCommentsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        id = int(self.get_argument('id',0))
        query = session.query(MemberComments).filter(MemberComments.food_ids.ilike("%_{0}_%".format(id)))
        list = query.order_by(MemberComments.id.desc()).limit(5).all()
        data_list = []
        if list:
            member_map = getDictFilterField(Member, Member.id, "id", selectFilterObj(list, "member_id"))
            for item in list:
                if item.member_id not in member_map:
                    continue
                tmp_member_info = member_map[item.member_id]
                tmp_data = {
                    'score': item.score_desc,
                    'date': item.created_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "content": item.content,
                    "user": {
                        'nickname': tmp_member_info.nickname,
                        'avatar_url': tmp_member_info.avatar,
                    }
                }
                data_list.append(tmp_data)
        resp['data']['list'] = data_list
        resp['data']['count'] = query.count()
        self.finish(resp)
