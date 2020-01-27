from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean



       
Base = declarative_base()


class Cat(Base):
   __tablename__ = 'cats'
   cat_id = Column(Integer, primary_key=True)
   name = Column(String)
   title= Column(String)
   story = Column(String)
   img = Column(String)

  
