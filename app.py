import os
from flask import Flask
from flask_cors import CORS, cross_origin


def create_app(test_config=None):

    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def be_cool():
        return "Hi"

    return app

app = create_app()

if __name__ == '__main__':
    app.run()