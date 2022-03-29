from typing import Optional
import os , logging
from sqlalchemy import table

from sqlmodel import Field, SQLModel, create_engine
from helper.table_helper import sunny




auth = f"{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}"
database = f"{os.getenv('DATABASE_URL')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
db = create_engine(f"mysql+pymysql://{auth}@{database}", pool_recycle=3600)

# Connecting db
try:
    db.connect()
    SQLModel.metadata.create_all(db)
    logging.info("Database connected successfully.")
except Exception as e: 
    logging.error(e)

