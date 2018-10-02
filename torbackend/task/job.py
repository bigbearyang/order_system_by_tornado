from __future__ import absolute_import
from common.libs.helper import getFormatDate,getCurrentDate
from models.member import Member
from models.pay import PayOrder
from models.stat import StatDailyFood,StatDailySite,StatDailyMember
from models.food import WxShareHistory,FoodSaleChangeLog
from sqlalchemy import func
import random
from models import session
import logging
from celery.schedules import crontab
from celery import Celery,platforms

platforms.C_FORCE_ROOT = True # linux下便于使用root权限运行

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='w')

worker = Celery("tasks",broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/1")
worker.conf['worker_hijack_root_logger'] = False # 让日志输出到文件，否则celery会拦截

date = getFormatDate(getCurrentDate(),"%Y-%m-%d")
date_from = date + " 00:00:00"
date_to = date + " 23:59:59"
params = {
    'date': date,
    'date_from': date_from,
    'date_to': date_to
}

# 会员统计
@worker.task()
def statMember(params):
    date = params['date']
    date_from = params['date_from']
    date_to = params['date_to']
    logging.info("act:{0},from:{1},to:{2}".format("会员统计", date_from, date_to))

    member_list = session.query(Member).all()
    if not member_list:
        logging.info("no member list")
        return

    for member_info in member_list:
        tmp_stat_member = session.query(StatDailyMember).filter_by(date=date, member_id=member_info.id).first()
        if tmp_stat_member:
            tmp_model_stat_member = tmp_stat_member
        else:
            tmp_model_stat_member = StatDailyMember()
            tmp_model_stat_member.date = date
            tmp_model_stat_member.member_id = member_info.id
            tmp_model_stat_member.created_time = getCurrentDate()

        tmp_stat_pay = session.query(func.sum(PayOrder.total_price).label("total_pay_money")) \
            .filter(PayOrder.member_id == member_info.id, PayOrder.status == 1) \
            .filter(PayOrder.created_time >= date_from, PayOrder.created_time <= date_to).first()
        tmp_stat_share_count = session.query(WxShareHistory).filter(PayOrder.member_id == member_info.id) \
            .filter(PayOrder.created_time >= date_from, PayOrder.created_time <= date_to).count()

        tmp_model_stat_member.total_shared_count = tmp_stat_share_count
        tmp_model_stat_member.total_pay_money = tmp_stat_pay[0] if tmp_stat_pay[0] else 0.00
        '''
        为了测试效果模拟数据，生产环境下请注释掉
        '''
        tmp_model_stat_member.total_shared_count = random.randint(50, 100)
        tmp_model_stat_member.total_pay_money = random.randint(1000, 1010)
        tmp_model_stat_member.updated_time = getCurrentDate()
        session.add(tmp_model_stat_member)
        session.commit()

    return

# food统计
@worker.task()
def statFood(params):
    date = params['date']
    date_from = params['date_from']
    date_to = params['date_to']
    logging.info("act:{0},from:{1},to:{2}".format("food统计", date_from, date_to))

    stat_food_list = session.query(FoodSaleChangeLog.food_id,
                                      func.sum(FoodSaleChangeLog.quantity).label("total_count"),
                                      func.sum(FoodSaleChangeLog.price).label("total_pay_money")) \
        .filter(FoodSaleChangeLog.created_time >= date_from, FoodSaleChangeLog.created_time <= date_to) \
        .group_by(FoodSaleChangeLog.food_id).all()

    if not stat_food_list:
        logging.info("no data")
        return

    for item in stat_food_list:
        tmp_food_id = item[0]
        tmp_stat_food = session.query(StatDailyFood).filter_by(date=date, food_id=tmp_food_id).first()
        if tmp_stat_food:
            tmp_model_stat_food = tmp_stat_food
        else:
            tmp_model_stat_food = StatDailyFood()
            tmp_model_stat_food.date = date
            tmp_model_stat_food.food_id = tmp_food_id
            tmp_model_stat_food.created_time = getCurrentDate()

        tmp_model_stat_food.total_count = item[1]
        tmp_model_stat_food.total_pay_money = item[2]
        tmp_model_stat_food.updated_time = getCurrentDate()

        '''
        为了测试效果模拟数据，生产环境下请注释掉
        '''
        tmp_model_stat_food.total_count = random.randint(50, 100)
        tmp_model_stat_food.total_pay_money = random.randint(1000, 1010)

        session.add(tmp_model_stat_food)
        session.commit()

    return

# site统计
@worker.task()
def statSite(params):
    date = params['date']
    date_from = params['date_from']
    date_to = params['date_to']
    logging.info( "act:{0},from:{1},to:{2}".format("site统计",date_from,date_to))

    stat_pay = session.query(func.sum(PayOrder.total_price).label("total_pay_money")) \
        .filter(PayOrder.status == 1) \
        .filter(PayOrder.created_time >= date_from, PayOrder.created_time <= date_to).first()

    stat_member_count = session.query(Member).count()
    stat_new_member_count = session.query(Member).filter(Member.created_time >= date_from,
                        Member.created_time <= date_to).count()

    stat_order_count = session.query(PayOrder).filter_by( status = 1 )\
        .filter(PayOrder.created_time >= date_from, PayOrder.created_time <= date_to)\
        .count()

    stat_share_count = session.query(WxShareHistory).filter(WxShareHistory.created_time >= date_from
        , WxShareHistory.created_time <= date_to).count()

    tmp_stat_site = session.query(StatDailySite).filter_by(date=date).first()
    if tmp_stat_site:
        tmp_model_stat_site = tmp_stat_site
    else:
        tmp_model_stat_site = StatDailySite()
        tmp_model_stat_site.date = date
        tmp_model_stat_site.created_time = getCurrentDate()

    tmp_model_stat_site.total_pay_money = stat_pay[ 0 ] if stat_pay[ 0 ] else 0.00
    tmp_model_stat_site.total_new_member_count = stat_new_member_count
    tmp_model_stat_site.total_member_count = stat_member_count
    tmp_model_stat_site.total_order_count = stat_order_count
    tmp_model_stat_site.total_shared_count = stat_share_count
    tmp_model_stat_site.updated_time = getCurrentDate()
    '''
    为了测试效果模拟数据，生产环境下请注释掉
    '''
    tmp_model_stat_site.total_pay_money = random.randint(1000, 1010)
    tmp_model_stat_site.total_new_member_count = random.randint(50, 100)
    tmp_model_stat_site.total_member_count += tmp_model_stat_site.total_new_member_count
    tmp_model_stat_site.total_order_count = random.randint(900, 1000)
    tmp_model_stat_site.total_shared_count = random.randint(1000, 2000)
    session.add(tmp_model_stat_site)
    session.commit()



worker.conf.update(
    timezone='Asia/Shanghai',
    enable_utc=True,
    beat_schedule={
        "task1": {
            "task": "task.job.statMember",
            "schedule": crontab(minute='*/120'), # 每隔2小时执行
            "args": (params,)
        },
        "task2": {
            "task": "task.job.statFood",
            "schedule": crontab(minute='*/120'),
            "args": (params,)
        },
        "task3": {
            "task": "task.job.statSite",
            "schedule": crontab(minute='*/120'),
            "args": (params,)
        }
    }
)