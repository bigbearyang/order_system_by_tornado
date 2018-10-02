from tornado.web import RequestHandler
from common.libs.member.memberservice import MemberService
from models.member import OauthMemberBind,Member
from models.food import WxShareHistory
from models import session
from common.libs.helper import getCurrentDate
from views.auth import ApiAuth

class WxLoginHandler(RequestHandler):
    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        code = self.get_argument('code',None)
        if code is None:
            resp['code'] = -1
            resp['msg'] = "需要code"
            self.write(resp)
            return

        openid = MemberService.getWeChatOpenId(code)
        if openid is None:
            resp['code'] = -1
            resp['msg'] = "调用微信出错"
            self.write(resp)
            return

        nickname = self.get_argument('nickName','')
        sex = self.get_argument('gender',0)
        avatar = self.get_argument('avatarUrl','')
        '''
            判断是否已经测试过，注册了直接返回一些信息
        '''
        bind_info = session.query(OauthMemberBind).filter_by(openid=openid, type=1).first()
        if not bind_info:
            model_member = Member()
            model_member.nickname = nickname
            model_member.sex = sex
            model_member.avatar = avatar
            model_member.salt = MemberService.geneSalt()
            model_member.updated_time = model_member.created_time = getCurrentDate()
            session.add(model_member)
            session.commit()

            model_bind = OauthMemberBind()
            model_bind.member_id = model_member.id
            model_bind.type = 1
            model_bind.openid = openid
            model_bind.extra = ''
            model_bind.updated_time = model_bind.created_time = getCurrentDate()
            session.add(model_bind)
            session.commit()

            bind_info = model_bind

        bind_info = session.query(OauthMemberBind).filter_by(openid=openid, type=1).first()
        if not bind_info:
            resp['code'] = -1
            resp['msg'] = "未绑定"
            self.write(resp)
            return

        member_info = session.query(Member).filter_by(id=bind_info.member_id).first()
        token = "%s#%s" % (MemberService.geneAuthCode(member_info), member_info.id)
        resp['data'] = {'token': token}
        self.finish(resp)

class WxCheckRegHandler(RequestHandler):
    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        code = self.get_argument('code','')
        if not code or len(code) < 1:
            resp['code'] = -1
            resp['msg'] = "需要code"
            self.write(resp)
            return

        openid = MemberService.getWeChatOpenId(code)
        if openid is None:
            resp['code'] = -1
            resp['msg'] = "调用微信出错"
            self.write(resp)
            return

        bind_info = session.query(OauthMemberBind).filter_by(openid=openid, type=1).first()
        if not bind_info:
            resp['code'] = -1
            resp['msg'] = "未绑定"
            self.write(resp)
            return

        member_info = session.query(Member).filter_by(id=bind_info.member_id).first()
        if not member_info:
            resp['code'] = -1
            resp['msg'] = "未查询到绑定信息"
            self.write(resp)
            return

        token = "%s#%s" % (MemberService.geneAuthCode(member_info), member_info.id)
        resp['data'] = {'token': token}
        self.finish(resp)

class WxMemberShareHandler(ApiAuth,RequestHandler):
    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        url = self.get_argument('url','')
        member_info = self.member_info
        member_info = None
        model_share = WxShareHistory()
        if member_info:
            model_share.member_id = member_info.id
        model_share.share_url = url
        model_share.created_time = getCurrentDate()
        session.add(model_share)
        session.commit()
        self.finish(resp)

class WxMemberInfoHandler(ApiAuth,RequestHandler):
    def get(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
        member_info = self.member_info
        resp['data']['info'] = {
            "nickname": member_info.nickname,
            "avatar_url": member_info.avatar
        }
        self.finish(resp)





