# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from config import config
from flask_moment import Moment

app = Flask(__name__)
"""
config
 -- 'default': DevelopmentConfig
 -- 'develop': DevelopmentConfig
 -- 'testing': TestingConfig
 -- 'production': ProductionConfig
    you can edit this in config.py
"""
config_name = 'default'
app.config.from_object(config[config_name])
config[config_name].init_app(app)
toolbar = DebugToolbarExtension(app)

moment = Moment()
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name=None, main=True):
    if config_name is None:
        config_name = 'default'
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    db.init_app(app)
    moment.init_app(app)
    toolbar.init_app(app)
    login_manager.init_app(app)

    from api import api
    app.register_blueprint(api, url_prefix="/api/v1.0")

    return app

app = create_app(config_name = 'default')




"""
blueprint
you can register a <blueprint> by run:
 -- mana blueprint <blueprint>
under app folder
"""
from api import api
app.register_blueprint(api,url_prefix="/api/v1.0")
