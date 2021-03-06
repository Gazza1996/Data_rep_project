from sqlalchemy.orm import sessionmaker
from table import *
# http://mindmapengineers.com/mmeblog/creating-web-app-scratch-using-python-flask-and-mysql-part-3
# database engine
engine = create_engine('sqlite:///bucketlist.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# user information
user = User("admin", "password")
session.add(user)

# commit the record the database
session.commit()
session.commit()
