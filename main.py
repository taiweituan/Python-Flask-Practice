import os

from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    error = None
    return render_template('index.html', error=error)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('email')
    password = request.form.get('password')
    print username
    print password
    return render_template('welcome.html', username=username)


if __name__ == '__main__':
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8081)))
