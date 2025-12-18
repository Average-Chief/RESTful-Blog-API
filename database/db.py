#sqlite setup

from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///blog.db"

engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

def get_session():
    return Session(engine)

def create_db():
    SQLModel.metadata.create_all(engine)