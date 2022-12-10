from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware

from database import session
from model import UserTable, User

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users")
def read_users():
    users = session.query(UserTable).all()
    
    return users

@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    
    return user

@app.post("/user")
def create_user(name: str, age: int):
    user = UserTable()
    
    user.name = name
    user.age = age
    
    session.add(user)
    session.commit()
    
    return f"{name} created..."

@app.put("/users")
def update_users(users: List[User]):
    
    for user_table in users:
        user = session.query(UserTable).filter(UserTable.id == user_table.id).first()
        user.name = user_table.name
        user.age = user_table.age
        session.commit()
    
    return f"업데이트 완료..."

@app.delete("/user")
def delete_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).delete()
    session.commit()
    
    return read_users