from flask import Flask as fl, render_template, json, request, redirect, session, jsonify
from flask.ext.mysql import MySQL
import sqlite3
from werkzeug import generate_password_hash, check_password_hash

DATABASE = 'data/data.db'

#mysql = MySQL()
app = fl(__name__)
#app.secret_key = 'G00319609'

# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'gary'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'gary'
#app.config['MYSQL_DATABASE_DB'] = 'bucketList'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)

def get_db():
    db = getattr(fl.g, '_database', None)
    if db is None:
        db = fl.g._database = sqlite3.connect(DATABASE)
    return db

@app.route("/")
def hello():
  cur = get_db().cursor()
  cur.execute("SELECT name FROM mydb")
  return str(cur.fetchall())

# calls index.html
@app.route('/')
def main():
    return render_template('index.html')

# calls signup.html
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

# calls bucketList.html
@app.route('/showBucketLIst')
def showBucketList():
    return render_template('bucketList.html')

# calls signin.html and userLink.html
@app.route('/showSignin')
def showSignin():
    if session.get('user'):
        return render_template('userLink.html')
    else:
        return render_template('signin.html')

# calls userLink.html
@app.route('/userLink')
def userHome():
    if session.get('user'):
        return render_template('userLink.html')

# calls to get a wish
@app.route('/getBucketList')
def getBucketList():
    try:
        if session.get('user'):
            _user = session.get('user')

            con = mysql.connect()
            cursor = con.cursor()
            cursor.callproc('sp_GetBucketListByUser', (_user,))
            bucketList = cursor.fetchall()

            wishes_dict = []
            for wish in bucketList:
                wish_dict = {
                    'Id': bucketList[0],
                    'Title': bucketList[1],
                    'Description': bucketList[2],
                    'Date': bucketList[4]}
                wishes_dict.append(wish_dict)

            return json.dumps(wishes_dict)
        else:
            return render_template('/')
    except Exception as e:
        return render_template('/', error=str(e))

# calls to add to bucketList
@app.route('/addBucketList', methods=['POST'])
def addBucketList():
    try:
        if session.get('user'):
            _title = request.form['inputTitle']
            _description = request.form['inputDescription']
            _user = session.get('user')

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_addBucketList', (_title, _description, _user))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return redirect('/userLink')
    finally:
        cursor.close()
        conn.close()

# method to validate login is correct
@app.route('/validateLogin', methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']

        # connect to mysql

        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('sp_validateLogin', (_username,))
        data = cursor.fetchall()

        if len(data) > 0:
            if check_password_hash(str(data[0][3]), _password):
                session['user'] = data[0][0]
                return redirect('/userLink')
    finally:
        cursor.close()
        con.close()

# validate correct sign up formats
@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:

            # All Good, let's call MySQL

            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser', (_name, _email, _hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message': 'User created successfully !'})
    finally:
        cursor.close()
        conn.close()

# method to run application
if __name__ == "__main__":
    app.run()