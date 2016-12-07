from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# https://github.com/data-representation/example-sqlite/blob/master/setup.py
# https://github.com/data-representation/example-sqlite/blob/master/webapp.py
# database engine
engine = create_engine('sqlite:///bucketlist.db', echo=True)
Base = declarative_base()

# setting up user information
class User(Base):
    __tablename__ = "users"

    # string for user information
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    # initiates username and password
    def __init__(self, username, password):
        self.username = username
        self.password = password

# create tables
Base.metadata.create_all(engine)
