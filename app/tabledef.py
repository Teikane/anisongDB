from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, DATE, DATETIME, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///anisong.db', echo=True)
Base = declarative_base()
 
########################################################################
class User(Base):
    """"""
    __tablename__ = "Users"
 
    id = Column(Integer, primary_key=True)
    email = Column(String(60), nullable = False, unique= True)
    username = Column(String(25), nullable = False, unique= True)
    password = Column(String(256), nullable = False)
    dob = DATE()
    gender = Column(String(1))
    create_time = DATETIME()

 
    #----------------------------------------------------------------------
    def __init__(self, email, username, password):
        """"""
        self.email = email
        self.username = username
        self.password = password
 
# create tables
Base.metadata.create_all(engine)