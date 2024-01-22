from models.user import Menu, Submenu, Dishes
from sqlalchemy.orm import Session
from dto import user
import psycopg2

def create_dishes(data:user.dish, db):
    user=Dishes(id=data.id, dish=data.dish,price=data.price)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

def get_dishes(id:int, db):
    return db.query(Dishes).filter(Dishes.id==id).first()

def get_dishesAll(db):
    return db.query(Dishes).all()


def update_dishes(data:user.dish, db, id:int):
    user = db.query(Dishes).filter(Dishes.id==id).first()
    user.dish = data.dish
    user.price=data.price
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

def remove_dishes(db:Session,id:int):
    user=db.query(Dishes).filter(Dishes.id==id).delete()
    try:
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user