from typing import List, Optional, Literal, TypeVar
from pydantic import BaseModel
from pydantic import Field
from pydantic.generics import GenericModel


# class menu(BaseModel):
#     id: Optional[int] = None
#     title: Optional[str] = None
#     submenu_count: Optional[int] = None
#     dishes_count: Optional[int] = None

#     class Config:
#         from_attributes = True

# class submenu(BaseModel):
#     id: Optional[int] = None
#     # dishes: List[str] = List
#     # dishes_count:Optional[int] = None
#     menu_id:Optional[int] = None

# class dish(BaseModel):
#     id: Optional[int] = None
#     dishc: Optional[str] = None
#     price: Optional[str] = None
#     submenu_id: Optional[int] = None


# ________________

# from sqlalchemy.orm import Mapped


# class menu(BaseModel):
#     id: Mapped[int] = None
#     title: Mapped[str] = None
#     submenu_count: Mapped[int] = None
#     dishes_count: Mapped[int] = None

#     class Config:
#         from_attributes = True

# class submenu(BaseModel):
#     id: Mapped[int] = None
#     menu_id:Mapped[int] = None

# class dish(BaseModel):
#     id: Mapped[int] = None
#     dishc: Mapped[str] = None
#     price: Mapped[str] = None
#     submenu_id: Mapped[int] = None


from sqlalchemy.orm import Mapped


class menu(BaseModel):
    id: int= None
    title: str= None
    submenus:list["submenu"]
    submenu_count: int = None
    dishes_count: int = None

    class Config:
        from_attributes = True

class submenu(BaseModel):
    id: int= None
    menu_id:int = None
    dishes:list["dish"]
    dishes_count: int
    menu_id: int
    menus:"menu"

class dish(BaseModel):
    id: int
    dishc: str 
    price: str 
    submenu_id: int 
    submenudishs: int

    class Config:
        from_attributes = True