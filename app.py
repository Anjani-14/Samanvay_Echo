from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def homePage():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug = True)
