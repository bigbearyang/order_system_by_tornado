# 路径相关配置
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/static/upload/',
    'prefix_url':'/static/upload/'
}

Server = {
    'domain':'http://127.0.0.1:8000'
}

STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}

PAY_STATUS_MAPPING = {
    "1":"已支付",
    "-8":"待支付",
    "0":"已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0":"订单关闭",
    "1":"支付成功",
    "-8":"待支付",
    "-7":"待发货",
    "-6":"待确认",
    "-5":"待评价"
}


# tornado 配置
settings = {
    'template_path':os.path.join(BASE_DIR,'templates'),
    'cookie_secert':'fsegegwrhrtwhtrhtwr',
    'static_path':os.path.join(BASE_DIR,'static'),
    'debug':True,
    "autoescape":None, # 关闭模板的所有转义
    "login_url":"/login",# 权限验证失败后会跳转到指定url，与get_current_user搭配使用

}

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'food_db'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}?charset=utf8'.format\
    (username=USERNAME,password=PASSWORD,hostname=HOSTNAME,port=PORT,database=DATABASE)

# 微信appid
appid = 'xxxxx'
appkey = 'yyyy'

