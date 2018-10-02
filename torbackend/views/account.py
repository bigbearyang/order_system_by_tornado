from tornado.web import RequestHandler
from models import session
from models.log import AppAccessLog
from models.user import User
from common.libs.helper import getCurrentDate
from common.libs.user import userservice
from views.auth import Auth
from sqlalchemy import or_
from config import STATUS_MAPPING

class AccountHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        mix_kw = self.get_argument('mix_kw','')
        status = self.get_argument('status','')
        query = session.query(User)
        if mix_kw:
            rule = or_(User.nickname.ilike("%{0}%".format(mix_kw)),
                       User.mobile.ilike("%{0}%".format(mix_kw)))
            query = query.filter(rule)
        if status:
            query = query.filter(User.status == int(status))
        list = query.order_by(User.uid.desc()).all()

        resp_data['list'] = list
        resp_data['search_con'] = {"mix_kw":mix_kw,"status":status,'p':1}
        resp_data['status_mapping'] = STATUS_MAPPING
        self.render("account/index.html", **resp_data)


class AccountInfoHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        uid = int(self.get_argument('id', 0))
        if uid < 1:
            self.redirect("/account/index")

        info = session.query(User).filter_by(uid=uid).first()
        if not info:
            self.redirect("/account/index")

        access_list = session.query(AppAccessLog).filter_by(uid=uid).order_by(AppAccessLog.id.desc()).limit(10).all()
        resp_data['info'] = info
        resp_data['access_list'] = access_list
        self.render("account/info.html", **resp_data)

class AccountSetHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        uid = int(self.get_argument('id',0))
        info = User(nickname='',mobile='',email='',login_name='',uid='')
        if uid:
            info = session.query(User).filter_by(uid=uid).first()
        resp_data['info'] = info
        self.render("account/set.html", **resp_data)

    def post(self, *args, **kwargs):
        default_pwd = "******"
        resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
        id = self.get_argument('id',0)
        nickname = self.get_argument('nickname','')
        mobile = self.get_argument('mobile','')
        email = self.get_argument('email','')
        login_name = self.get_argument('login_name','')
        login_pwd = self.get_argument('login_pwd','')

        if nickname is None or len(nickname) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的姓名~~"
            self.finish(resp)
            return

        if mobile is None or len(mobile) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的手机号码~~"
            self.finish(resp)
            return

        if email is None or len(email) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的邮箱~~"
            self.finish(resp)
            return

        if login_name is None or len(login_name) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的登录用户名~~"
            self.finish(resp)
            return

        if login_pwd is None or len(email) < 6:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的登录密码~~"
            self.finish(resp)
            return

        has_in = session.query(User).filter(User.login_name == login_name, User.uid != id).first()
        if has_in:
            resp['code'] = -1
            resp['msg'] = "该登录名已存在，请换一个试试~~"
            self.finish(resp)
            return

        user_info = session.query(User).filter_by(uid=id).first()
        if user_info:
            model_user = user_info
        else:
            model_user = User()
            model_user.created_time = getCurrentDate()
            model_user.login_salt = userservice.geneSalt()

        model_user.nickname = nickname
        model_user.mobile = mobile
        model_user.email = email
        model_user.login_name = login_name
        if login_pwd != default_pwd:
            if user_info and user_info.uid == 1:
                resp['code'] = -1
                resp['msg'] = "该用户是演示账号，不准修改密码和登录用户名~~"
                self.finish(resp)

            model_user.login_pwd = userservice.genePwd(login_pwd, model_user.login_salt)

        model_user.updated_time = getCurrentDate()
        session.add(model_user)
        session.commit()
        self.finish(resp)

class AccountOpsHandler(Auth,RequestHandler):
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
            return

        user_info = session.query(User).filter_by(uid=id).first()
        if not user_info:
            resp['code'] = -1
            resp['msg'] = "指定账号不存在~~"
            self.finish(resp)
            return

        if act == "remove":
            user_info.status = 0
        elif act == "recover":
            user_info.status = 1

        if user_info and user_info.uid == 1:
            resp['code'] = -1
            resp['msg'] = "该用户是演示账号，不准操作账号~~"
            self.finish(resp)
            return

        user_info.update_time = getCurrentDate()
        session.add(user_info)
        session.commit()
        self.finish(resp)

