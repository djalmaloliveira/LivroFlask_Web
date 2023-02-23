# https://www.youtube.com/watch?v=r40pC9kyoj0
# https://www.youtube.com/watch?v=Pz9rayiDHW0
# https://palletsprojects.com/p/flask/

from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Hello, World! - 4"

# if __name__ == '__main__':
#     app.run(debug=True)
    
from app.controllers import default
