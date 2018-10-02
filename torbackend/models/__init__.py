from config import DB_URI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# echo=True，表示显示sql语句到控制台
engine = create_engine(DB_URI,echo=False)

# 所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(engine)


Session = sessionmaker(bind=engine)  # sessionmaker是一个类
session = Session() # Session是一个对象，内部实现了__call__方法

__all__ = ['session','Base']