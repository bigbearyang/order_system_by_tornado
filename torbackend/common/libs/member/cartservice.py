from models.member import MemberCart
from common.libs.helper import getCurrentDate
from models import session

class CartService():

    @staticmethod
    def deleteItem( member_id = 0,items = None ):
        if member_id < 1 or not items:
            return False
        for item in items:
            session.query(MemberCart).filter_by(food_id = item['id'],member_id = member_id).delete()
        session.commit()
        return True

    @staticmethod
    def setItems( member_id = 0,food_id = 0,number = 0 ):
        if member_id < 1 or food_id < 1 or number < 1:
            return False
        cart_info = session.query(MemberCart).filter_by(food_id = food_id, member_id= member_id).first()
        if cart_info:
            model_cart = cart_info
        else:
            model_cart = MemberCart()
            model_cart.member_id = member_id
            model_cart.created_time = getCurrentDate()

        model_cart.food_id = food_id
        model_cart.quantity = number
        model_cart.updated_time = getCurrentDate()
        session.add(model_cart)
        session.commit()
        return True

