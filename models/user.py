from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from database import Base

class Menu(Base):
    __tablename__='Menu'
    id=Column(Integer, primary_key=True, index=True)
    title =Column(String)
    submenu_count =Column(Integer)
    dishes_count =Column(Integer)

class Submenu(Base):
    __tablename__='SubMenu'
    id=Column(Integer, primary_key=True, index=True)
    dishes =Column(String)
    dishes_count =Column(Integer)

class Dishes(Base):
    __tablename__='Dishes'
    id=Column(Integer, primary_key=True, index=True)
    dish =Column(String, unique=True, index=True)
    price =Column(String, index=True)