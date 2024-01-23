from sqlalchemy import ForeignKey
from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class menu(Base):
    __tablename__="TableMenu"
    id: Mapped[int]=mapped_column(primary_key=True)
    # dishc: Mapped[str]
    # submenus = relationship("submenu", back_populates="menus", cascade="all, delete-orphan")
    # submenu_count =Mapped[int]
    # dishes_count =Mapped[int]

class submenu(Base):
    __tablename__="TableSubmenu"
    id: Mapped[int]=mapped_column(primary_key=True)
    # dishes:Mapped[list["dish"]] = relationship(
    #     back_populates="submenudish",)
    # dishes_count: Mapped[int]
    # menu_id:Mapped[int]=mapped_column(ForeignKey("TableMenu.id", ondelete="CASCADE"))
    # menus:Mapped["menu"]=relationship(back_populates="submenus",)


class dish(Base):
    __tablename__="TableDish"
    id: Mapped[int]=mapped_column(primary_key=True)
    dishc: Mapped[str]
    price: Mapped[str]
    submenu_id:Mapped[int]  #=mapped_column(ForeignKey("TableSubmenu.id", ondelete="CASCADE"))
    submenudishs:Mapped[str] #=relationship(back_populates="dishes",)"submenu"

# class menu(Base):
#     __tablename__="TableMenu"
#     id=Column(Integer, primary_key=True, index=True)
#     title =Column(String)
#     submenus = relationship("submenu", back_populates="menus", cascade="all, delete-orphan")
#     submenu_count =Column(Integer)
#     dishes_count =Column(Integer)

# class submenu(Base):
#     __tablename__="TableSubmenu"
#     id=Column(Integer, primary_key=True, index=True)
#     dishes =relationship("dish", back_populates="submenudish", cascade="all, delete-orphan")
#     dishes_count =Column(Integer)
#     menu_id =Column(Integer, ForeignKey("TableMenu.id"))
#     menus=relationship("menu", back_populates="submenus")

# class dish(Base):
#     __tablename__="TableDish"
#     id=Column(Integer, primary_key=True, index=True, autoincrement="auto")
#     dishc =Column(String)
#     price =Column(String)
#     submenu_id =Column(Integer, ForeignKey("TableSubmenu.id"))
#     submenudish=relationship("submenu", back_populates="dishes")