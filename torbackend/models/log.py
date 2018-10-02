from sqlalchemy import BigInteger, Column, DateTime, Integer, String, Text
from sqlalchemy.schema import FetchedValue
from models import Base

class AppAccessLog(Base):
    __tablename__ = 'app_access_log'

    id = Column(Integer, primary_key=True)
    uid = Column(BigInteger, nullable=False, index=True, server_default=FetchedValue())
    referer_url = Column(String(255), nullable=False, server_default=FetchedValue())
    target_url = Column(String(255), nullable=False, server_default=FetchedValue())
    query_params = Column(Text, nullable=False)
    ua = Column(String(255), nullable=False, server_default=FetchedValue())
    ip = Column(String(32), nullable=False, server_default=FetchedValue())
    note = Column(String(1000), nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())

class AppErrorLog(Base):
    __tablename__ = 'app_error_log'

    id = Column(Integer, primary_key=True)
    referer_url = Column(String(255), nullable=False, server_default=FetchedValue())
    target_url = Column(String(255), nullable=False, server_default=FetchedValue())
    query_params = Column(Text, nullable=False)
    content = Column(String, nullable=False)
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())
