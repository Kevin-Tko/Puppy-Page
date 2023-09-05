from flask import Flask, render_template, redirect, url_for

def name():
    print('Kevin')
######Creating my app######
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'mysecretkey'



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)