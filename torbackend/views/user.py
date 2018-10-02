from tornado.web import RequestHandler
from common.libs.user.userservice import UserService
from models.user import User
from models import session
from .session import Session
from views.auth import Auth

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('user/login.html')

    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '登录成功~~', 'data': {}}
        login_name = self.get_argument('login_name')
        login_pwd = self.get_argument('login_pwd')

        if login_name is None or len(login_name) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入正确的登录用户名~~"
            self.write(resp)
            return

        if login_pwd is None or len(login_pwd) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入正确的邮箱密码~~"
            self.write(resp)
            return

        user_info = session.query(User).filter_by(login_name=login_name).first()
        if user_info is None:
            resp['code'] = -1
            resp['msg'] = "请输入正确的登录用户名和密码-1~~"
            self.write(resp)
            return

        if user_info.login_pwd != UserService.genePwd(login_pwd, user_info.login_salt):
            resp['code'] = -1
            resp['msg'] = "请输入正确的登录用户名和密码-2~~"
            self.write(resp)
            return

        if user_info.status != 1:
            resp['code'] = -1
            resp['msg'] = "账号已被禁用，请联系管理员处理~~"
            self.write(resp)
            return

        sess = Session(self)
        sess['user'] = user_info
        resp = {'code': 200, 'msg': '登录成功~~'}
        self.finish(resp)

class UserEditHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        self.render("user/edit.html", **{'current': 'edit'})

    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        nickname = self.get_argument('nickname','')
        email = self.get_argument('email','')

        if nickname is None or len(nickname) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的姓名~~"
            self.write(resp)
            return

        if email is None or len(email) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的邮箱~~"
            self.write(resp)
            return

        user_info = self.current_user
        user_info.nickname = nickname
        user_info.email = email

        session.add(user_info)
        session.commit()
        self.finish(resp)

class UserRestPwdHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        self.render("user/reset_pwd.html", **{'current': 'reset-pwd'})

    def post(self, *args, **kwargs):

        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}

        old_password = self.get_argument('old_password','')
        new_password = self.get_argument('new_password','')
        if old_password is None or len(old_password) < 6:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的原密码~~"
            self.write(resp)
            return

        if new_password is None or len(new_password) < 6:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的新密码~~"
            self.write(resp)
            return

        if old_password == new_password:
            resp['code'] = -1
            resp['msg'] = "请重新输入一个吧，新密码和原密码不能相同哦~~"
            self.write(resp)
            return

        user_info = self.current_user

        if user_info.uid == 1:
            resp['code'] = -1
            resp['msg'] = "该用户是演示账号，不准修改密码和登录用户名~~"
            self.write(resp)
            return

        user_info.login_pwd = UserService.genePwd(new_password, user_info.login_salt)

        session.add(user_info)
        session.commit()
        self.clear_all_cookies()
        sess = Session(self)
        sess['user'] = user_info
        resp = {'code': 200, 'msg': '登录成功~~'}
        self.finish(resp)

class UserLogoutHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        print(Session.container)
        Session.container.pop(self.nid)
        print(Session.container)
        self.redirect('/login')












