from sqlalchemy import Column, Date, DateTime, Index, Integer, Numeric
from sqlalchemy.schema import FetchedValue
from models import Base

class StatDailyFood(Base):
    __tablename__ = 'stat_daily_food'
    __table_args__ = (
        Index('date_food_id', 'date', 'food_id'),
    )

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    food_id = Column(Integer, nullable=False, server_default=FetchedValue())
    total_count = Column(Integer, nullable=False, server_default=FetchedValue())
    total_pay_money = Column(Numeric(10, 2), nullable=False, server_default=FetchedValue())
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())


class StatDailyMember(Base):
    __tablename__ = 'stat_daily_member'
    __table_args__ = (
        Index('idx_date_member_id', 'date', 'member_id'),
    )

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    member_id = Column(Integer, nullable=False, server_default=FetchedValue())
    total_shared_count = Column(Integer, nullable=False, server_default=FetchedValue())
    total_pay_money = Column(Numeric(10, 2), nullable=False, server_default=FetchedValue())
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())


class StatDailySite(Base):
    __tablename__ = 'stat_daily_site'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, index=True)
    total_pay_money = Column(Numeric(10, 2), nullable=False, server_default=FetchedValue())
    total_member_count = Column(Integer, nullable=False)
    total_new_member_count = Column(Integer, nullable=False)
    total_order_count = Column(Integer, nullable=False)
    total_shared_count = Column(Integer, nullable=False)
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())
