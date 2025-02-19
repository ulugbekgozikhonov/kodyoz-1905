# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base

# engine = create_engine('sqlite:///database.db', echo=True)
# Base = declarative_base()

from sqlalchemy.ext.asyncio import create_async_engine
import os

DB_URI = os.getenv('DB_URI', 'postgresql+psycopg2://postgres:root_123@localhost:5432/kodyoz1905')

engine = create_async_engine(DB_URI, echo=True)