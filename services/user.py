from models.user import menu, submenu, dish
from sqlalchemy.orm import Session
from sqlalchemy import func
from dto import user
import psycopg2

#Dish
def create_dishes(data:user.dish, db):
    user=dish(id=data.id, dishc=data.dishc,price=data.price, submenu_id=data.submenu_id)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

def get_dishes(id:int, db):
    return db.query(dish).filter(dish.id==id).first()

def get_dishesAll(db):
    return db.query(dish).all()

def update_dishes(data:user.dish, db, id:int):
    user = db.query(dish).filter(dish.id==id).first()
    user.dishc = data.dishc
    user.price=data.price
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

def remove_dishes(db:Session,id:int):
    user=db.query(dish).filter(dish.id==id).delete()
    try:
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

#Submenu
def create_submenu(data:user.submenu, db):
    dishes1=db.query(dish).all()
    user=submenu(id=data.id,dishes=dishes1, dishes_count=len(dishes1),menu_id=data.menu_id)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

def get_submenuAll(db):
    return db.query(submenu).all()

def get_submenu(id:int, db):
    return db.query(submenu).filter(submenu.id==id).first()

def update_submenu(data:user.submenu, db, id:int):
    user = db.query(submenu).filter(submenu.id==id).first()
    dishes1=db.query(dish).all()
    user.id = data.id
    user.dishes=dishes1
    user.dishes_count=len(dishes1)
    user.menu_id=data.menu_id
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

def remove_submenu(db:Session,id:int):
    user=db.query(submenu).filter(submenu.id==id).delete()
    try:
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

#Menu
def create_menu(data:user.menu, db):
    submenu1=db.query(submenu).all()
    dishes1=db.query(submenu.dishes).all()
    user=menu(id=data.id,submenus=submenu1, submenu_count=len(submenu1),dishes_count=len(dishes1))
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

def get_menuAll(db):
    return db.query(menu).all()

def get_menu(id:int, db):
    return db.query(menu).filter(menu.id==id).first()

def update_menu(data:user.menu, db, id:int):
    user = db.query(menu).filter(menu.id==id).first()
    submenu1=db.query(submenu).all()
    dishes1=db.query(dish).all()
    user.id = data.id
    user.submenus=submenu1
    user.submenu_count=len(submenu1)
    user.dishes_count=len(dishes1)
    
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

def remove_menu(db:Session,id:int):
    user=db.query(menu).filter(menu.id==id).delete()
    try:
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user