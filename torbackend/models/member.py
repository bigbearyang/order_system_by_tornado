from sqlalchemy import BigInteger, Column, DateTime, Integer, String, Index,Text
from sqlalchemy.schema import FetchedValue
from models import Base


class Member(Base):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(100), nullable=False, server_default=FetchedValue())
    mobile = Column(String(11), nullable=False, server_default=FetchedValue())
    sex = Column(Integer, nullable=False, server_default=FetchedValue())
    avatar = Column(String(200), nullable=False, server_default=FetchedValue())
    salt = Column(String(32), nullable=False, server_default=FetchedValue())
    reg_ip = Column(String(100), nullable=False, server_default=FetchedValue())
    status = Column(Integer, nullable=False, server_default=FetchedValue())
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())

    @property
    def status_desc(self):
        status_mapping = {
            "1": "正常",
            "0": "已删除"
        }
        return status_mapping[str(self.sex)]

    @property
    def sex_desc(self):
        sex_mapping = {
            "0":"未知",
            "1":"男",
            "2":"女"
        }
        return sex_mapping[str(self.sex)]
    
    
class MemberAddress(Base):
    __tablename__ = 'member_address'
    __table_args__ = (
        Index('idx_member_id_status', 'member_id', 'status'),
    )

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, nullable=False, server_default=FetchedValue())
    nickname = Column(String(20), nullable=False, server_default=FetchedValue())
    mobile = Column(String(11), nullable=False, server_default=FetchedValue())
    province_id = Column(Integer, nullable=False, server_default=FetchedValue())
    province_str = Column(String(50), nullable=False, server_default=FetchedValue())
    city_id = Column(Integer, nullable=False, server_default=FetchedValue())
    city_str = Column(String(50), nullable=False, server_default=FetchedValue())
    area_id = Column(Integer, nullable=False, server_default=FetchedValue())
    area_str = Column(String(50), nullable=False, server_default=FetchedValue())
    address = Column(String(100), nullable=False, server_default=FetchedValue())
    status = Column(Integer, nullable=False, server_default=FetchedValue())
    is_default = Column(Integer, nullable=False, server_default=FetchedValue())
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())



class MemberCart(Base):
    __tablename__ = 'member_cart'

    id = Column(Integer, primary_key=True)
    member_id = Column(BigInteger, nullable=False, index=True, server_default=FetchedValue())
    food_id = Column(Integer, nullable=False, server_default=FetchedValue())
    quantity = Column(Integer, nullable=False, server_default=FetchedValue())
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    
class MemberComments(Base):
    __tablename__ = 'member_comments'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, nullable=False, index=True, server_default=FetchedValue())
    food_ids = Column(String(200), nullable=False, server_default=FetchedValue())
    pay_order_id = Column(Integer, nullable=False, server_default=FetchedValue())
    score = Column(Integer, nullable=False, server_default=FetchedValue())
    content = Column(String(200), nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())

    @property
    def score_desc(self):
        score_map = {
            "10": "好评",
            "6": "中评",
            "0": "差评",
        }
        return score_map[ str( self.score ) ]
    
    
class OauthMemberBind(Base):
    __tablename__ = 'oauth_member_bind'
    __table_args__ = (
        Index('idx_type_openid', 'type', 'openid'),
    )

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, nullable=False, server_default=FetchedValue())
    client_type = Column(String(20), nullable=False, server_default=FetchedValue())
    type = Column(Integer, nullable=False, server_default=FetchedValue())
    openid = Column(String(80), nullable=False, server_default=FetchedValue())
    unionid = Column(String(100), nullable=False, server_default=FetchedValue())
    extra = Column(Text, nullable=False)
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())