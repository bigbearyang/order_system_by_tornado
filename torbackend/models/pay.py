from sqlalchemy import BigInteger, Column, DateTime, Index, Integer, Numeric, String, Text
from sqlalchemy.schema import FetchedValue
from models import Base
from config import PAY_STATUS_DISPLAY_MAPPING


class PayOrder(Base):
    __tablename__ = 'pay_order'
    __table_args__ = (
        Index('idx_member_id_status', 'member_id', 'status'),
    )

    id = Column(Integer, primary_key=True)
    order_sn = Column(String(40), nullable=False, unique=True, server_default=FetchedValue())
    member_id = Column(BigInteger, nullable=False, server_default=FetchedValue())
    total_price = Column(Numeric(10, 2), nullable=False, server_default=FetchedValue())
    yun_price = Column(Numeric(10, 2), nullable=False, server_default=FetchedValue())
    pay_price = Column(Numeric(10, 2), nullable=False, server_default=FetchedValue())
    pay_sn = Column(String(128), nullable=False, server_default=FetchedValue())
    prepay_id = Column(String(128), nullable=False, server_default=FetchedValue())
    note = Column(Text, nullable=False)
    status = Column(Integer, nullable=False, server_default=FetchedValue())
    express_status = Column(Integer, nullable=False, server_default=FetchedValue())
    express_address_id = Column(Integer, nullable=False, server_default=FetchedValue())
    express_info = Column(String(100), nullable=False, server_default=FetchedValue())
    comment_status = Column(Integer, nullable=False, server_default=FetchedValue())
    pay_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())


    @property
    def pay_status(self):
        tmp_status = self.status
        if self.status == 1:
            tmp_status = self.express_status
            if self.express_status == 1 and self.comment_status == 0:
                tmp_status = -5
            if self.express_status == 1 and self.comment_status == 1:
                tmp_status = 1
        return tmp_status

    @property
    def status_desc(self):
        return PAY_STATUS_DISPLAY_MAPPING[ str( self.pay_status )]

    @property
    def order_number(self):
        order_number = self.created_time.strftime("%Y%m%d%H%M%S")
        order_number = order_number + str(self.id).zfill(5)
        return order_number

class PayOrderItem(Base):
    __tablename__ = 'pay_order_item'

    id = Column(Integer, primary_key=True)
    pay_order_id = Column(Integer, nullable=False, index=True, server_default=FetchedValue())
    member_id = Column(BigInteger, nullable=False, server_default=FetchedValue())
    quantity = Column(Integer, nullable=False, server_default=FetchedValue())
    price = Column(Numeric(10, 2), nullable=False, server_default=FetchedValue())
    food_id = Column(Integer, nullable=False, index=True, server_default=FetchedValue())
    note = Column(Text, nullable=False)
    status = Column(Integer, nullable=False, server_default=FetchedValue())
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())
