from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from table import *

engine = create_engine('sqlite:///bucketlist.db', echo=True)

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('signin.html')
    else:
        return "Hello User!"

@app.route('/showBucketList', methods=['POST'])
def do_admin_showBucketList():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

# calls index.html
#@app.route('/')
#def main():
    #return render_template('index.html')

# calls bucketList.html
#@app.route('/showBucketLIst')
#def showBucketList():
    #return render_template('bucketList.html')

# calls signin.html and userLink.html
"""
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

 calls to add to bucketList
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


 method to validate login is correct

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
"""
# method to run application
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()