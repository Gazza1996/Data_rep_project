from flask import Flask, render_template, session, redirect
from flask.ext.mysql import MySQL
#from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)
app.secret_key= "G00319609"

# SQL configuration
app.config['MYSQL_DATABASE_USER'] = 'gary'
app.config['MYSQL_DATABASE_PASSWORD'] = 'gary'
app.config['MYSQL_DATABASE_DB'] = 'bucketlist'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/showSignin')
def showSignin():
    if session.get('user'):
        return render_template('userLink.html')
    else:
        return render_template('signin.html')

@app.route('/showBucketList')
def showBucketList():
    return render_template('bucketList.html')

# @app.route('/logout')
#def logout():
 #   session.pop('user',None)
  #  return redirect('/')


@app.route('/userLink')
def userHome():
    if session.get('user'):
        return render_template('userLink.html')


if __name__ == "__main__":
    app.run()