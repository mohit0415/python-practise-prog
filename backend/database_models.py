from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String


Base = declarative_base()


class Product(Base):

    __tablename__='product'


    id = Column(Integer,index=True,primary_key=True)
    name = Column(String(100),nullable=False)
    price = Column(Integer,nullable=False)
    qty = Column(Integer,nullable=False)


class Professor(Base):

    __tablename__='professor'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100))
    age = Column(Integer)
    subject = Column(String(100))
    qual = Column(String(100))