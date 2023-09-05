from flask import Flask, render_template, redirect, url_for



######Creating my app######
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'mysecretkey'

def name():
    print('Kevin')
name()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)