from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# database engine
engine = create_engine('sqlite:///bucketlist.db', echo=True)
Base = declarative_base()

# setting up user information
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

# create tables
Base.metadata.create_all(engine)