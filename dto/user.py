from typing import List, Optional, Literal, TypeVar
from pydantic import BaseModel
from pydantic import Field
from pydantic.generics import GenericModel


class menu(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    submenu_count: Optional[int] = None
    dishes_count: Optional[int] = None

    class Config:
        from_attributes = True

class submenu(BaseModel):
    id: Optional[int] = None
    # dishes: List[str] = List
    # dishes_count:Optional[int] = None
    menu_id:Optional[int] = None

class dish(BaseModel):
    id: Optional[int] = None
    dishc: Optional[str] = None
    price: Optional[str] = None
    submenu_id: Optional[int] = None

