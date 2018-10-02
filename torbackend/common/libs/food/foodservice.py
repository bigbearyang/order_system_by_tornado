from models import session
from models.food import FoodStockChangeLog,Food
from common.libs.helper import getCurrentDate

class FoodService():

    @staticmethod
    def setStockChangeLog(food_id = 0,quantity = 0,note = ''):

        if food_id < 1:
            return False

        food_info = session.query(Food).filter_by(id = food_id).first()
        if not food_info:
            return False

        model_stock_change = FoodStockChangeLog()
        model_stock_change.food_id = food_id
        model_stock_change.unit = quantity
        model_stock_change.total_stock = food_info.stock
        model_stock_change.note = note
        model_stock_change.created_time = getCurrentDate()
        session.add(model_stock_change)
        session.commit()
        return True


