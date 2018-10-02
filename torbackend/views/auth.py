import tornado.web
from models.member import Member
from models import session
from common.libs.member.memberservice import MemberService
from .session import Session

class Auth(tornado.web.RequestHandler):
    def prepare(self):
        self.current_user_info = self.check_user_login()
        if self.current_user_info:
            self.nid = self.current_user_info[0]
            self.current_user = self.current_user_info[1]['user']
            pass
        else:
            self.redirect('/login')

    def check_user_login(self):
        nid = self.get_cookie('Session_id')
        if nid:
            if nid in Session.container:
                return (nid,Session.container.get(nid))
            else:
                return None
        else:
            return None


class ApiAuth(tornado.web.RequestHandler):
    def prepare(self):
        self.member_info = self.check_member_login()
        if self.member_info:
            pass
        else:
            resp = {'code': -1, 'msg': '未登录~', 'data': {}}
            self.finish(resp)

    def check_member_login(self):
        auth_cookie = self.request.headers.get("Authorization")

        if auth_cookie is None:
            return False

        auth_info = auth_cookie.split("#")
        if len(auth_info) != 2:
            return False

        try:
            member_info = session.query(Member).filter_by(id=auth_info[1]).first()
        except Exception:
            return False

        if member_info is None:
            return False

        if auth_info[0] != MemberService.geneAuthCode(member_info):
            return False

        if member_info.status != 1:
            return False

        return member_info


