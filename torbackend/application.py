import tornado.web
from config import settings
from views.user import LoginHandler,UserEditHandler,UserLogoutHandler,UserRestPwdHandler
from views.index import IndexHandler
from views.account import AccountHandler,AccountInfoHandler,AccountSetHandler,AccountOpsHandler
from views.member import MemberHandler,MemberInfoHandler,MemberOpsHandler,MemberCommentHandler,MemberSetHandler
from views.food import FoodHandler,FoodInfoHandler,FoodCatHandler,FoodSetHandler,FoodCatSetHandler,FoodCatOpsHandler,FoodOpsHandler
from views.upload import UeditorHandler,UploadPicHandler
from views.finance import FinanceIndexHandler,FinancePayInfoHandler,FinanceAccountHandler,FinanceOderOpsHandler
from views.stat import StatIndexHandler,StatFoodHandler,StatMemberHandler,StatShareHandler
from views.chart import ChartFinanceHandler,ChartShareHandler,ChartDashboardHandler
from api.member import WxLoginHandler,WxCheckRegHandler,WxMemberInfoHandler,WxMemberShareHandler
from api.food import WxFoodIndexHandler,WxFoodSearchHandler,WxFoodCommentsHandler,WxFoodInfoHandler
from api.cart import WxCartIndexHandler,WxCartSetHandler,WxCartDelHandler
from api.address import WxAddressIndexHandler,WxAddressInfoHandler,WxAddressOptHandler,WxAddressSetHandler
from api.order import WxOrderCreateHandler,WxOrderInfoHandler,WxOrderOpsHandler,WxOrderPayHandler
from api.my import WxMyOrderHandler,WxMyCommentAddHandler,WxMyCommentListHandler,WxMyOrderInfoHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/login',LoginHandler),
            (r'/user/edit', UserEditHandler),
            (r'/user/logout', UserLogoutHandler),
            (r'/user/reset-pwd', UserRestPwdHandler),


            (r'/account/index', AccountHandler),
            (r'/account/info', AccountInfoHandler),
            (r'/account/set', AccountSetHandler),
            (r'/account/ops', AccountOpsHandler),

            (r'/member/index', MemberHandler),
            (r'/member/info', MemberInfoHandler),
            (r'/member/set', MemberSetHandler),
            (r'/member/comment', MemberCommentHandler),
            (r'/member/ops', MemberOpsHandler),

            (r'/food/index', FoodHandler),
            (r'/food/info', FoodInfoHandler),
            (r'/food/cat', FoodCatHandler),
            (r'/food/cat-set', FoodCatSetHandler),
            (r'/food/set', FoodSetHandler),
            (r'/food/ops', FoodOpsHandler),
            (r'/food/catops', FoodCatOpsHandler),

            (r'/upload/ueditor', UeditorHandler),
            (r'/upload/pic', UploadPicHandler),

            (r'/finance/index', FinanceIndexHandler),
            (r'/finance/pay-info', FinancePayInfoHandler),
            (r'/finance/account', FinanceAccountHandler),
            (r'/finance/ops', FinanceOderOpsHandler),

            (r'/stat/index', StatIndexHandler),
            (r'/stat/food', StatFoodHandler),
            (r'/stat/member', StatMemberHandler),
            (r'/stat/share', StatShareHandler),
            (r'/chart/finance', ChartFinanceHandler),
            (r'/chart/share', ChartShareHandler),
            (r'/chart/dashboard', ChartDashboardHandler),

            (r'/api/member/login', WxLoginHandler),
            (r'/api/member/check-reg', WxCheckRegHandler),
            (r'/api/food/index', WxFoodIndexHandler),
            (r'/api/food/search', WxFoodSearchHandler),
            (r'/api/food/info', WxFoodInfoHandler),
            (r'/api/food/comments', WxFoodCommentsHandler),
            (r'/api/member/info', WxMemberInfoHandler),
            (r'/api/member/share', WxMemberShareHandler),
            (r'/api/cart/index', WxCartIndexHandler),
            (r'/api/cart/set', WxCartSetHandler),
            (r'/api/cart/del', WxCartDelHandler),
            (r'/api/my/address/index', WxAddressIndexHandler),
            (r'/api/my/address/set', WxAddressSetHandler),
            (r'/api/my/address/info', WxAddressInfoHandler),
            (r'/api/my/address/ops', WxAddressOptHandler),
            (r'/api/my/order', WxMyOrderHandler),
            (r'/api/my/order/info', WxMyOrderInfoHandler),
            (r'/api/my/comment/add', WxMyCommentAddHandler),
            (r'/api/my/comment/list', WxMyCommentListHandler),
            (r'/api/order/info', WxOrderInfoHandler),
            (r'/api/order/create', WxOrderCreateHandler),
            (r'/api/order/pay', WxOrderPayHandler),
            (r'/api/order/ops', WxOrderOpsHandler),

        ]
        super(Application, self).__init__(handlers,**settings)

