from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship   #создание взаимосвязи

class menu(Base):
    __tablename__="TableMenu"
    id=Column(Integer, primary_key=True, index=True)
    title =Column(String)
    submenus = relationship("submenu", back_populates="menus", cascade="all, delete-orphan")
    submenu_count =Column(Integer)
    dishes_count =Column(Integer)

class submenu(Base):
    __tablename__="TableSubmenu"
    id=Column(Integer, primary_key=True, index=True)
    dishes =relationship("dish", back_populates="submenudish", cascade="all, delete-orphan")
    dishes_count =Column(Integer)
    menu_id =Column(Integer, ForeignKey("TableMenu.id"))
    menus=relationship("menu", back_populates="submenus")

class dish(Base):
    __tablename__="TableDish"
    id=Column(Integer, primary_key=True, index=True, autoincrement="auto")
    dishc =Column(String)
    price =Column(String)
    submenu_id =Column(Integer, ForeignKey("TableSubmenu.id"))
    submenudish=relationship("submenu", back_populates="dishes")