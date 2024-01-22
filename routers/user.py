from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, relationship
from database import get_db

from services import user as UserService
from dto import user as UserDTO


router=APIRouter()

# @router.get("/")
# async def root():
#     return {"message": "hello world"}

#Dish
@router.post('/v1/menus//submenus//dishes',tags=["user"])
async def create(data:UserDTO.dish=None, db:Session=Depends(get_db)):
    return UserService.create_dishes(data,db)

@router.get('/v1/menus//submenus//dishes',tags=["user"])
async def get(db:Session=Depends(get_db)):
    return UserService.get_dishesAll(db)

@router.get('/v1/menus//submenus//dishes/{id}',tags=["user"])
async def get(id:int=None, db:Session=Depends(get_db)):
    return UserService.get_dishes(id, db)

@router.patch("/v1/menus//submenus//dishes/{id}",tags=["user"])
async def update(id:int=None,data:UserDTO.dish=None, db:Session=Depends(get_db)):
    return UserService.update_dishes(data,db,id)

@router.delete("/v1/menus//submenus//dishes/{id}",tags=["user"])
async def delete(id:int=None, db: Session =Depends(get_db)):
    return UserService.remove_dishes(db, id)

#Submenu
@router.post('/v1/menus//submenus',tags=["user"])
async def create(data:UserDTO.submenu=None, db:Session=Depends(get_db)):
    return UserService.create_submenu(data,db)

@router.get('/v1/menus//submenus',tags=["user"])
async def get(db:Session=Depends(get_db)):
    return UserService.get_submenuAll(db)

@router.get('/v1/menus//submenus/{id}',tags=["user"])
async def get(id:int=None, db:Session=Depends(get_db)):
    return UserService.get_submenu(id, db)

@router.patch("/v1/menus//submenus/{id}",tags=["user"])
async def update(id:int=None,data:UserDTO.submenu=None, db:Session=Depends(get_db)):
    return UserService.update_submenu(data,db,id)

@router.delete("/v1/menus//submenus/{id}",tags=["user"])
async def delete(id:int=None, db: Session =Depends(get_db)):
    return UserService.remove_submenu(db, id)

#Menu
@router.post('/v1/menus',tags=["user"])
async def create(data:UserDTO.menu=None, db:Session=Depends(get_db)):
    return UserService.create_menu(data,db)

@router.get('/v1/menus',tags=["user"])
async def get(db:Session=Depends(get_db)):
    return UserService.get_menuAll(db)

@router.get('/v1/menus/{id}',tags=["user"])
async def get(id:int=None, db:Session=Depends(get_db)):
    return UserService.get_menu(id, db)

@router.patch("/v1/menus/{id}",tags=["user"])
async def update(id:int=None,data:UserDTO.submenu=None, db:Session=Depends(get_db)):
    return UserService.update_menu(data,db,id)

@router.delete("/v1/menus/{id}",tags=["user"])
async def delete(id:int=None, db: Session =Depends(get_db)):
    return UserService.remove_menu(db, id)