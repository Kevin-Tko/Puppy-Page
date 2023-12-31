from flask import Flask, render_template, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate  import Migrate

######  Creating my app  ######
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'mysecretkey'

######   Creating my SQLITE database and configuring my app ######
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)