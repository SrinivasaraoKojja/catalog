from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from flask_login import Usermixin

Base=declarative_base()

class Register(Base):
	__tablename__='register'

	id=Column(Integer,primary_key=True)
	name=Column(String(100))
	surname=Column(String(100))
	mobile=Column(String(20))
	email=Column(String(50))
	branch=Column(String(10))
	role=Column(String(50))

class User(Base,Usermixin):
	__tablename__='user'

	id=Column(Integer,primary_key=True)
	name=Column(String(100))
	email=Column(String(50))
	password=Column(String(50))



engine=create_engine('sqlite:///iii.db')
Base.metadata.create_all(engine)
print("Database is created...")


 
