<<<<<<< HEAD
import sqlite3

DATABASE = 'data/data.db'

def database_db():
  #Creates database if it has not already been set up
  db = sqlite3.connect(DATABASE)
  cur = db.cursor()

  # Create the table if it doesn't exist
  cur.execute("CREATE TABLE IF NOT EXISTS mydb(id INTEGER PRIMARY KEY, name TEXT)")
  db.commit()

  # Insert some dummy data if the table is empty
  cur.execute("SELECT COUNT(*) FROM mydb")
  if cur.fetchall()[0][0] == 0:
    cur.execute('INSERT INTO mydb(name) VALUES("Gary")')
    cur.execute('INSERT INTO mydb(email) VALUES("Gary")')
    cur.execute('INSERT INTO mydb(password) VALUES("Enter")')
    db.commit()

if __name__ == "__main__":
=======
import sqlite3

DATABASE = 'data/data.db'

def database_db():
  #Creates database if it has not already been set up
  db = sqlite3.connect(DATABASE)
  cur = db.cursor()

  # Create the table if it doesn't exist
  cur.execute("CREATE TABLE IF NOT EXISTS mydb(id INTEGER PRIMARY KEY, name TEXT)")
  db.commit()

  # Insert some dummy data if the table is empty
  cur.execute("SELECT COUNT(*) FROM mydb")
  if cur.fetchall()[0][0] == 0:
    cur.execute('INSERT INTO mydb(name) VALUES("Gary")')
    cur.execute('INSERT INTO mydb(email) VALUES("Gary")')
    cur.execute('INSERT INTO mydb(password) VALUES("Enter")')
    db.commit()

if __name__ == "__main__":
>>>>>>> 9683876fee63c13d362ae7d5e9d2f5fbfb7d6508
  database_db()