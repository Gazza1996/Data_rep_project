from sqlalchemy.orm import sessionmaker
from table import *
# database engine
engine = create_engine('sqlite:///bucketlist.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin", "password")
session.add(user)

# commit the record the database
session.commit()
session.commit()