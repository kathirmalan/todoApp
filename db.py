from sqlmodel import SQLModel, create_engine

# It is necessary to import all the models for the engine to create tables
from models import tasks


sqlite_file_name = "/Users/kathirmalan/Projects/SQL_LITE/sql_model.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
