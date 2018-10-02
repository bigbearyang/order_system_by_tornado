from tornado.web import RequestHandler
from models import session
from models.pay import PayOrder
from models.food import Food
from models.member import Member,MemberComments
from config import STATUS_MAPPING
from common.libs.helper import getCurrentDate,getDictFilterField,selectFilterObj
from views.auth import Auth

class MemberHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        query = session.query(Member)
        mix_kw = self.get_argument('mix_kw','')
        status = self.get_argument('status','')

        if mix_kw:
            query = query.filter(Member.nickname.ilike("%{0}%".format(mix_kw)))

        if status :
            query = query.filter(Member.status == int(status))

        list = query.order_by(Member.id.desc()).limit(100).all()

        resp_data['list'] = list
        resp_data['search_con'] = {'status':status,'mix_kw':mix_kw,'p':1}
        resp_data['status_mapping'] = STATUS_MAPPING
        resp_data['current'] = 'index'
        self.render("member/index.html", **resp_data)

class MemberInfoHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        id = int(self.get_argument("id", 0))
        if id < 1:
            self.redirect('/member/index')

        info = session.query(Member).filter_by(id=id).first()
        if not info:
            self.redirect('/member/index')

        pay_order_list = session.query(PayOrder).filter_by(member_id=id).filter(PayOrder.status.in_([-8, 1])) \
            .order_by(PayOrder.id.desc()).all()
        comment_list = session.query(MemberComments).filter_by(member_id=id).order_by(MemberComments.id.desc()).all()

        resp_data['info'] = info
        resp_data['pay_order_list'] = pay_order_list
        resp_data['comment_list'] = comment_list
        resp_data['current'] = 'index'
        self.render("member/info.html", **resp_data)

class MemberSetHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):

        resp_data = {}
        id = int(self.get_argument("id", 0))
        if id < 1:
            self.redirect("/member/index")

        info = session.query(Member).filter_by(id=id).first()
        if not info:
            self.redirect("/member/index")

        if info.status != 1:
            self.redirect("/member/index")

        resp_data['info'] = info
        resp_data['current'] = 'index'
        self.render("member/set.html", **resp_data)

    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
        id = self.get_argument('id',0)
        nickname = self.get_argument('nickname','')
        if nickname is None or len(nickname) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的姓名~~"
            self.write(resp)
            return

        member_info = session.query(Member).filter_by(id=id).first()
        if not member_info:
            resp['code'] = -1
            resp['msg'] = "指定会员不存在~~"
            self.write(resp)
            return

        member_info.nickname = nickname
        member_info.updated_time = getCurrentDate()
        session.add(member_info)
        session.commit()
        self.finish(resp)

class MemberCommentHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        query = session.query(MemberComments)
        comment_list = query.order_by(MemberComments.id.desc()).limit(100).all()
        data_list = []
        if comment_list:
            member_map = getDictFilterField(Member, Member.id, "id", selectFilterObj(comment_list, "member_id"))
            food_ids = []
            for item in comment_list:
                tmp_food_ids = (item.food_ids[1:-1]).split("_")
                tmp_food_ids = {}.fromkeys(tmp_food_ids).keys()
                food_ids = food_ids + list(tmp_food_ids)

            food_map = getDictFilterField(Food, Food.id, "id", food_ids)

            for item in comment_list:
                tmp_member_info = member_map[item.member_id]
                tmp_foods = []
                tmp_food_ids = (item.food_ids[1:-1]).split("_")
                for tmp_food_id in tmp_food_ids:
                    tmp_food_info = food_map[int(tmp_food_id)]
                    tmp_foods.append({
                        'name': tmp_food_info.name,
                    })

                tmp_data = {
                    "content": item.content,
                    "score": item.score,
                    "member_info": tmp_member_info,
                    "foods": tmp_foods
                }
                data_list.append(tmp_data)
        resp_data['list'] = data_list
        resp_data['current'] = 'comment'

        self.render("member/comment.html", **resp_data)

class MemberOpsHandler(Auth,RequestHandler):
    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
        id = self.get_argument('id',0)
        act = self.get_argument('act','')

        if not id:
            resp['code'] = -1
            resp['msg'] = "请选择要操作的账号~~"
            self.finish(resp)
            return

        if act not in ['remove', 'recover']:
            resp['code'] = -1
            resp['msg'] = "操作有误，请重试~~"
            self.finish(resp)

        member_info = session.query(Member).filter_by(id=id).first()
        if not member_info:
            resp['code'] = -1
            resp['msg'] = "指定会员不存在~~"
            self.finish(resp)
            return

        if act == "remove":
            member_info.status = 0
        elif act == "recover":
            member_info.status = 1

        member_info.updated_time = getCurrentDate()
        session.add(member_info)
        session.commit()
        self.finish(resp)
