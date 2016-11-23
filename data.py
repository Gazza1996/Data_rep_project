from flask import Flask, render_template
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

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()