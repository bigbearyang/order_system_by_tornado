from common.libs.helper import getFormatDate
from models.stat import StatDailySite
import datetime
from views.auth import Auth
from tornado.web import RequestHandler
from models import session

class ChartDashboardHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        now = datetime.datetime.now()
        date_before_30days = now + datetime.timedelta(days=-30)
        date_from = getFormatDate(date=date_before_30days, format="%Y-%m-%d")
        date_to = getFormatDate(date=now, format="%Y-%m-%d")

        list = session.query(StatDailySite).filter(StatDailySite.date >= date_from) \
            .filter(StatDailySite.date <= date_to).order_by(StatDailySite.id.asc()) \
            .all()

        resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
        data = {
            "categories": [],
            "series": [
                {
                    "name": "会员总数",
                    "data": []
                },
                {
                    "name": "订单总数",
                    "data": []
                },
            ]
        }

        if list:
            for item in list:
                data['categories'].append(getFormatDate(date=item.date, format="%Y-%m-%d"))
                data['series'][0]['data'].append(item.total_member_count)
                data['series'][1]['data'].append(item.total_order_count)

        resp['data'] = data
        self.finish(resp)

class ChartFinanceHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        now = datetime.datetime.now()
        date_before_30days = now + datetime.timedelta(days=-30)
        date_from = getFormatDate(date=date_before_30days, format="%Y-%m-%d")
        date_to = getFormatDate(date=now, format="%Y-%m-%d")

        list = session.query(StatDailySite).filter(StatDailySite.date >= date_from) \
            .filter(StatDailySite.date <= date_to).order_by(StatDailySite.id.asc()) \
            .all()

        resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
        data = {
            "categories": [],
            "series": [
                {
                    "name": "日营收报表",
                    "data": []
                }
            ]
        }

        if list:
            for item in list:
                data['categories'].append(getFormatDate(date=item.date, format="%Y-%m-%d"))
                data['series'][0]['data'].append(float(item.total_pay_money))

        resp['data'] = data
        self.finish(resp)

class ChartShareHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        now = datetime.datetime.now()
        date_before_30days = now + datetime.timedelta(days=-30)
        date_from = getFormatDate(date=date_before_30days, format="%Y-%m-%d")
        date_to = getFormatDate(date=now, format="%Y-%m-%d")

        list = session.query(StatDailySite).filter(StatDailySite.date >= date_from) \
            .filter(StatDailySite.date <= date_to).order_by(StatDailySite.id.asc()) \
            .all()
        resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
        data = {
            "categories": [],
            "series": [
                {
                    "name": "日分享",
                    "data": []
                }
            ]
        }
        if list:
            for item in list:
                data['categories'].append(getFormatDate(date=item.date, format="%Y-%m-%d"))
                data['series'][0]['data'].append(item.total_shared_count)

        resp['data'] = data
        self.finish(resp)
