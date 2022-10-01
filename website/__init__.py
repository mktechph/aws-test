#all codes defined here will run automatically

from datetime import timedelta
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sikreto'
    app.permanent_session_lifetime = timedelta(seconds=5)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
    