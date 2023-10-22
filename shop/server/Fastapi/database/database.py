from sqlmodel import Field, SQLModel
from typing import Optional
from .engine import engine


class User(SQLModel, table=True):
    __tablename__ = 'user'

    user_id: Optional[int] = Field(default=None, primary_key=True)
    user_name: str = Field(nullable=False)
    user_age: int = Field(nullable=False)



def init():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    init()
