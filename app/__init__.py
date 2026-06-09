from flask import Flask

from .views import admin


def create_app():
    app = Flask(__name__)
    app.register_blueprint(admin)
    return app
