# import psycopg2
# try:
#     conn=psycopg2.connect("postgresql://postgres:7475@127.0.0.1:5432")
#     print ("yes")
# except Exception as e:
#     print ("cant")
#     print(e)






import uvicorn
from fastapi import FastAPI
from database import engine, Base
from routers import user as UserRouter

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(UserRouter.router, prefix="/api", tags=["user"])

if __name__=='__main__':
     uvicorn.run("main:app", host='localhost',port=8000,reload=True)

