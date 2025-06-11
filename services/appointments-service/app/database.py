import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


##MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
##MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
##MYSQL_USER = os.getenv("MYSQL_USER", "root")
##MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "Libertadores.")
##MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "appointments_db")
##
##DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
##
##engine = create_engine(DATABASE_URL)
##
##SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
##
##Base = declarative_base()
