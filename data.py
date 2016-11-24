from flask import Flask, render_template, session, redirect, request, jsonify
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)
app.secret_key= "G00319609"

# SQL configuration
app.config['MYSQL_DATABASE_USER'] = 'gary'
app.config['MYSQL_DATABASE_PASSWORD'] = 'gary'
app.config['MYSQL_DATABASE_DB'] = 'bucketlist'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# calls the index.html file
@app.route("/")
def main():
    return render_template('index.html')

# calls signup.html
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

# calls signin.html and userLink.html
@app.route('/showSignin')
def showSignin():
    if session.get('user'):
        return render_template('userLink.html')
    else:
        return render_template('signin.html')

# calls bucketList.html
@app.route('/showBucketList')
def showBucketList():
    return render_template('bucketList.html')

# @app.route('/logout')
#def logout():
 #   session.pop('user',None)
  #  return redirect('/')

# calls userLink.html
@app.route('/userLink')
def userHome():
    if session.get('user'):
        return render_template('userLink.html')

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

# route to sign up method
@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate name, email and password
        if _name and _email and _password:

            # call MySQL

            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser', (_name, _email, _hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message': 'User created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run()