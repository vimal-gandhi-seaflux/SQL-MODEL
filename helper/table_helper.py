from sqlmodel import Field, SQLModel, create_engine
from typing import Optional


class sunny(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

class vimal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

class yash(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    secret_name: str
    age: Optional[int] = None
    
    