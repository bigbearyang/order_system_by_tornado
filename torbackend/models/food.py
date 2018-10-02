from sqlalchemy import BigInteger, Column, DateTime, Integer, String,Numeric
from sqlalchemy.schema import FetchedValue
from models import Base

class Food(Base):
    __tablename__ = 'food'

    id = Column(Integer, primary_key=True)
    cat_id = Column(Integer, nullable=False, server_default=FetchedValue())
    name = Column(String(100), nullable=False, server_default=FetchedValue())
    price = Column(Numeric(10, 2), nullable=False, server_default=FetchedValue())
    main_image = Column(String(100), nullable=False, server_default=FetchedValue())
    summary = Column(String(2000), nullable=False, server_default=FetchedValue())
    stock = Column(Integer, nullable=False, server_default=FetchedValue())
    tags = Column(String(200), nullable=False, server_default=FetchedValue())
    status = Column(Integer, nullable=False, server_default=FetchedValue())
    month_count = Column(Integer, nullable=False, server_default=FetchedValue())
    total_count = Column(Integer, nullable=False, server_default=FetchedValue())
    view_count = Column(Integer, nullable=False, server_default=FetchedValue())
    comment_count = Column(Integer, nullable=False, server_default=FetchedValue())
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())


class FoodCat(Base):
    __tablename__ = 'food_cat'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(50), nullable=False, server_default=FetchedValue())
    weight = Column(Integer, nullable=False, server_default=FetchedValue())
    status = Column(Integer, nullable=False, server_default=FetchedValue())
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())

    @property
    def status_desc(self):
        status_mapping = {
            "1": "正常",
            "0": "已删除"
        }
        return status_mapping[str(self.status)]


class FoodSaleChangeLog(Base):
    __tablename__ = 'food_sale_change_log'

    id = Column(Integer, primary_key=True)
    food_id = Column(Integer, nullable=False, index=True, server_default=FetchedValue())
    quantity = Column(Integer, nullable=False, server_default=FetchedValue())
    price = Column(Numeric(10, 2), nullable=False, server_default=FetchedValue())
    member_id = Column(Integer, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())


class FoodStockChangeLog(Base):
    __tablename__ = 'food_stock_change_log'

    id = Column(Integer, primary_key=True)
    food_id = Column(Integer, nullable=False, index=True)
    unit = Column(Integer, nullable=False, server_default=FetchedValue())
    total_stock = Column(Integer, nullable=False, server_default=FetchedValue())
    note = Column(String(100), nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())


class WxShareHistory(Base):
    __tablename__ = 'wx_share_history'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, nullable=False, server_default=FetchedValue())
    share_url = Column(String(200), nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())
