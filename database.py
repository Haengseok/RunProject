from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

USER_NAME = 'root'
USER_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_NAME = 'root'
PORT = 3306

DB_URL = f"mysql+pymysql://{USER_NAME}:{USER_PASSWORD}@{DB_HOST}:{PORT}/{DB_NAME}?charset=utf8"

ENGINE = create_engine(
    DB_URL,
    encoding = "utf-8"
)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()