from sqlmodel import SQLModel, create_engine, Session
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:28092004@localhost:7004/trending_db1")

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    """
    Tạo tất cả tables trong database
    """
    SQLModel.metadata.create_all(engine)

def get_session():
    """
    Dependency để lấy database session
    """
    with Session(engine) as session:
        yield session