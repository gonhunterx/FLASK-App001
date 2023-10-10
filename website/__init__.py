# This is going to make the website folder a python package.
# so we can import it and what is inside this folder will run automatically.

from flask import Flask


def create_app():
    # initalize flask
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "whatever secret string i want here."

    from .views import views
    from .auth import auth

    # registering the blueprints here
    app.register_blueprint(views, url_prefiix="/")
    app.register_blueprint(auth, url_prefiix="/")

    return app
