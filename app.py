#D:\Work\Livros_do_Copel\Flask_Web_Development_Developing.pdf 


from flask import Flask, render_template, redirect, url_for
from flask import request



app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name



@app.route('/userAgent')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent




if __name__ == '__main__':
    app.run(debug=True)