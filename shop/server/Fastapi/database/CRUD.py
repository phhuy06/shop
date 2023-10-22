from .session import SQL
from .database import User

def create_user(user: User):
    return SQL(action="create", tables=[User], data=user)

def read_user(id : int):
    condition = (User.user_id == id)
    return SQL(action="read", tables=[User], condition=condition)

def update_user(id : int, user: User):
    condition = (User.user_id == id)
    return SQL(action="update", tables=[User], condition=condition, data=user)

def delete_user(id : int):
    condition = (User.user_id == id)
    return SQL(action="delete", tables=[User], condition=condition)


