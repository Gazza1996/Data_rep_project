from flask import Flask, render_template, json, request, redirect, session, jsonify
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)
app.secret_key = 'G00319609'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'gary'
app.config['MYSQL_DATABASE_PASSWORD'] = 'gary'
app.config['MYSQL_DATABASE_DB'] = 'bucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

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
def showAddWish():
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

#@app.route('/logout')
#def logout():
 #   session.pop('user', None)
  #  return redirect('/')

# calls to get a wish
@app.route('/getWish')
def getWish():
    try:
        if session.get('user'):
            _user = session.get('user')

            con = mysql.connect()
            cursor = con.cursor()
            cursor.callproc('sp_GetWishByUser', (_user,))
            wishes = cursor.fetchall()

            wishes_dict = []
            for wish in wishes:
                wish_dict = {
                    'Id': wish[0],
                    'Title': wish[1],
                    'Description': wish[2],
                    'Date': wish[4]}
                wishes_dict.append(wish_dict)

            return json.dumps(wishes_dict)
        else:
            return render_template('/')
    except Exception as e:
        return render_template('/', error=str(e))

# calls to add a wish
@app.route('/addWish', methods=['POST'])
def addWish():
    try:
        if session.get('user'):
            _title = request.form['inputTitle']
            _description = request.form['inputDescription']
            _user = session.get('user')

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_addWish', (_title, _description, _user))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return redirect('/userHome')
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
                return redirect('/userHome')
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