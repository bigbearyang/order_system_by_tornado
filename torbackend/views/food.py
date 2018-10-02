from tornado.web import RequestHandler
from models.food import Food,FoodCat,FoodStockChangeLog
from models import session
from common.libs.helper import getCurrentDate, getDictFilterField
from decimal import Decimal
from common.libs.food.foodservice import FoodService
from views.auth import Auth
from sqlalchemy import  or_
from config import STATUS_MAPPING

class FoodHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        mix_kw = self.get_argument('mix_kw','')
        status = self.get_argument('status','')
        cat_id = self.get_argument('cat_id', '')
        query = session.query(Food)
        if mix_kw:
            rule = or_(Food.name.ilike("%{0}%".format(mix_kw)), Food.tags.ilike("%{0}%".format('mix_kw')))
            query = query.filter(rule)

        if status:
            query = query.filter(Food.status == int(status))

        if cat_id:
            query = query.filter(Food.cat_id == int(cat_id))

        list = query.order_by(Food.id.desc()).limit(100).all()
        print(cat_id,status,mix_kw)
        cat_mapping = getDictFilterField(FoodCat, FoodCat.id, "id", [])
        resp_data['list'] = list
        resp_data['search_con'] = {'status':status,'cat_id':cat_id,'mix_kw':mix_kw,'p':1}
        resp_data['status_mapping'] = STATUS_MAPPING
        resp_data['cat_mapping'] = cat_mapping
        resp_data['current'] = 'index'
        self.render("food/index.html", **resp_data)

class FoodCatSetHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        id = int(self.get_argument('id',0))
        info = session.query(FoodCat).filter_by(id = id).first()
        if info is None:
            info = FoodCat()
        current = 'cat'
        self.render('food/cat_set.html', info=info, current=current)

    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
        id = int(self.get_argument('id', 0))
        weight = int(self.get_argument('weight', 0))
        name = self.get_argument('name', '')

        if name is None or len(name) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的分类名称~~"
            self.write(resp)
            return

        food_cat_info = session.query(FoodCat).filter_by(id=id).first()
        if food_cat_info:
            model_food_cat = food_cat_info
        else:
            model_food_cat = FoodCat()
            model_food_cat.created_time = getCurrentDate()
        model_food_cat.name = name
        model_food_cat.weight = weight
        model_food_cat.updated_time = getCurrentDate()
        session.add(model_food_cat)
        session.commit()
        self.write(resp)
        return


class FoodSetHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        id = int(self.get_argument('id',[0])[0])
        info = session.query(Food).filter_by(id=id).first()
        if info is None:
            info = Food()
        cat_list = session.query(FoodCat).all()
        current = 'index'
        self.render("food/set.html",info=info,cat_list=cat_list,current=current)

    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
        id = int(self.get_argument('id',0))
        cat_id = int(self.get_argument('cat_id',0))
        name = self.get_argument('name','')
        price = self.get_argument('price','')
        main_image = self.get_argument('main_image','')
        summary = self.get_argument('summary','')
        stock = int(self.get_argument('stock',''))
        tags = self.get_argument('tags','')

        if cat_id < 1:
            resp['code'] = -1
            resp['msg'] = "请选择分类~~"
            self.finish(resp)
            return

        if name is None or len(name) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的名称~~"
            self.finish(resp)
            return

        if not price or len(price) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的售卖价格~~"
            self.finish(resp)
            return

        price = Decimal(price).quantize(Decimal('0.00'))
        if price <= 0:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的售卖价格~~"
            self.finish(resp)
            return

        if main_image is None or len(main_image) < 3:
            resp['code'] = -1
            resp['msg'] = "请上传封面图~~"
            self.finish(resp)
            return

        if summary is None or len(summary) < 3:
            resp['code'] = -1
            resp['msg'] = "请输入图书描述，并不能少于10个字符~~"
            self.finish(resp)
            return

        if stock < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的库存量~~"
            self.finish(resp)
            return

        if tags is None or len(tags) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入标签，便于搜索~~"
            self.finish(resp)
            return

        food_info = session.query(Food).filter_by(id=id).first()
        before_stock = 0
        if food_info:
            model_food = food_info
            before_stock = model_food.stock
        else:
            model_food = Food()
            model_food.status = 1
            model_food.created_time = getCurrentDate()

        model_food.cat_id = cat_id
        model_food.name = name
        model_food.price = price
        model_food.main_image = main_image
        model_food.summary = summary
        model_food.stock = stock
        model_food.tags = tags
        model_food.updated_time = getCurrentDate()

        session.add(model_food)
        session.commit()

        FoodService.setStockChangeLog(model_food.id, int(stock) - int(before_stock), "后台修改")
        self.finish(resp)

class FoodInfoHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        id = int(self.get_argument('id',0))
        if id < 1:
            self.redirect("/food/index")

        info = session.query(Food).filter_by(id=id).first()
        if not info:
            self.redirect("/food/index")

        stock_change_list = session.query(FoodStockChangeLog).filter(FoodStockChangeLog.food_id == id) \
            .order_by(FoodStockChangeLog.id.desc()).all()

        resp_data['info'] = info
        resp_data['stock_change_list'] = stock_change_list
        resp_data['current'] = 'index'
        self.render("food/info.html", **resp_data)

class FoodSetHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        id = int(self.get_argument('id',0))
        info = Food(id=0,name='',cat_id='',price='',main_image='',summary='',stock='',tags='')
        if id != 0:
            info = session.query(Food).filter_by(id=id).first()
        if not info:
            self.redirect('/food/index')
        cat_list = session.query(FoodCat).all()
        resp_data['info'] = info
        resp_data['cat_list'] = cat_list
        resp_data['current'] = 'index'
        self.render("food/set.html", **resp_data)

    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
        id = int(self.get_argument('id',0))
        cat_id = int(self.get_argument('cat_id',0))
        name = self.get_argument('name','')
        price = self.get_argument('price',0)
        main_image = self.get_argument('main_image',0)
        summary = self.get_argument('summary','')
        stock = self.get_argument('stock','')
        tags = self.get_argument('tags','')

        if cat_id < 1:
            resp['code'] = -1
            resp['msg'] = "请选择分类~~"
            self.finish(resp)
            return

        if name is None or len(name) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的名称~~"
            self.finish(resp)
            return

        if not price or len(price) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的售卖价格~~"
            self.finish(resp)
            return

        price = Decimal(price).quantize(Decimal('0.00'))
        if price <= 0:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的售卖价格~~"
            self.finish(resp)
            return

        if main_image is None or len(main_image) < 3:
            resp['code'] = -1
            resp['msg'] = "请上传封面图~~"
            self.finish(resp)
            return

        if summary is None or len(summary) < 3:
            resp['code'] = -1
            resp['msg'] = "请输入图书描述，并不能少于10个字符~~"
            self.finish(resp)
            return

        if summary is None:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的库存量~~"
            self.finish(resp)
            return

        if tags is None or len(tags) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入标签，便于搜索~~"
            self.finish(resp)
            return

        food_info = session.query(Food).filter_by(id=id).first()
        before_stock = 0
        if food_info:
            model_food = food_info
            before_stock = model_food.stock
        else:
            model_food = Food()
            model_food.status = 1
            model_food.created_time = getCurrentDate()

        model_food.cat_id = cat_id
        model_food.name = name
        model_food.price = price
        model_food.main_image = main_image
        model_food.summary = summary
        model_food.stock = stock
        model_food.tags = tags
        model_food.updated_time = getCurrentDate()

        session.add(model_food)
        session.commit()

        FoodService.setStockChangeLog(model_food.id, int(stock) - int(before_stock), "后台修改")
        self.finish(resp)

class FoodCatSetHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        id = int(self.get_argument("id", 0))
        info = FoodCat(name="",weight="",id=0)
        if id != 0:
            info = FoodCat.query.filter_by(id=id).first()
        resp_data['info'] = info
        resp_data['current'] = 'cat'
        self.render("food/cat_set.html", **resp_data)

    def post(self, *args, **kwargs):
        resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
        id = self.get_argument('id',0)
        name = self.get_argument('name','')
        weight = int(self.get_argument('weight',1))

        if name is None or len(name) < 1:
            resp['code'] = -1
            resp['msg'] = "请输入符合规范的分类名称~~"
            self.finish(resp)
            return

        food_cat_info = session.query(FoodCat).filter_by(id=id).first()
        if food_cat_info:
            model_food_cat = food_cat_info
        else:
            model_food_cat = FoodCat()
            model_food_cat.created_time = getCurrentDate()
        model_food_cat.name = name
        model_food_cat.weight = weight
        model_food_cat.updated_time = getCurrentDate()
        session.add(model_food_cat)
        session.commit()
        self.finish(resp)


class FoodCatHandler(Auth,RequestHandler):
    def get(self, *args, **kwargs):
        resp_data = {}
        status = self.get_argument('status','')
        query = session.query(FoodCat)
        if status:
            query = query.filter(FoodCat.status == int(status))
        list = query.order_by(FoodCat.weight.desc(), FoodCat.id.desc()).all()
        resp_data['list'] = list
        resp_data['search_con'] = {'status':status}
        resp_data['status_mapping'] = STATUS_MAPPING
        resp_data['current'] = 'cat'
        self.render("food/cat.html", **resp_data)

class FoodCatOpsHandler(Auth,RequestHandler):
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

        food_cat_info = session.query(FoodCat).filter_by(id=id).first()
        if not food_cat_info:
            resp['code'] = -1
            resp['msg'] = "指定分类不存在~~"
            self.finish(resp)
            return

        if act == "remove":
            food_cat_info.status = 0
        elif act == "recover":
            food_cat_info.status = 1

            food_cat_info.update_time = getCurrentDate()
        session.add(food_cat_info)
        session.commit()
        self.finish(resp)


class FoodOpsHandler(Auth,RequestHandler):
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

        food_info = session.query(Food).filter_by(id=id).first()
        if not food_info:
            resp['code'] = -1
            resp['msg'] = "指定美食不存在~~"
            self.finish(resp)
            return

        if act == "remove":
            food_info.status = 0
        elif act == "recover":
            food_info.status = 1

        food_info.updated_time = getCurrentDate()
        session.add(food_info)
        session.commit()
        self.finish(resp)
