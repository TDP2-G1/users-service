import logging
import os

from flasgger import Swagger
from flask import Flask
from flask_cors import CORS

import usersServiceApp.commands
import usersServiceApp.database
import usersServiceApp.model
from usersServiceApp.api.admin import bp_admin
from usersServiceApp.api.block import bp_block
from usersServiceApp.api.feedback import bp_feedback
from usersServiceApp.api.follower import bp_follower
from usersServiceApp.api.genre import bp_genre
from usersServiceApp.api.home_info import bp_homeinfo
from usersServiceApp.api.language import bp_language
from usersServiceApp.api.level import bp_level
from usersServiceApp.api.login import bp_login
from usersServiceApp.api.report import bp_report
from usersServiceApp.api.report_type import bp_report_type
from usersServiceApp.api.user import bp_user


def create_app(my_config=None):
    # setup app
    app = Flask(__name__)
    # setup CORS
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    # setup with the configuration provided by the user / environment
    if my_config is None:
        app.config.from_object(os.environ['APP_SETTINGS'])
    else:
        app.config.from_object(my_config)
    # setup all our dependencies, for now only database using application factory pattern
    database.init_app(app)
    commands.init_app(app)

    CORS(bp_homeinfo)  # enable CORS on the bp_stinfo blue print
    CORS(bp_user)  # enable CORS on the bp_stinfo blue print
    CORS(bp_genre)  # enable CORS on the bp_stinfo blue print
    CORS(bp_language)  # enable CORS on the bp_stinfo blue print
    CORS(bp_level)  # enable CORS on the bp_stinfo blue print
    CORS(bp_feedback)
    CORS(bp_follower)
    CORS(bp_report_type)
    CORS(bp_report)
    CORS(bp_block)
    CORS(bp_admin)
    CORS(bp_login)


    @app.before_first_request
    def create_db():
        database.create_tables()

    app.register_blueprint(bp_homeinfo)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_genre)
    app.register_blueprint(bp_language)
    app.register_blueprint(bp_level)
    app.register_blueprint(bp_feedback)
    app.register_blueprint(bp_follower)
    app.register_blueprint(bp_report_type)
    app.register_blueprint(bp_report)
    app.register_blueprint(bp_block)
    app.register_blueprint(bp_admin)
    app.register_blueprint(bp_login)

    # setup swagger
    swagger = Swagger(app)

    # setup logging
    logging.basicConfig(filename='error.log', level=logging.DEBUG)
    app.logger.info('New session started. Database up and running')

    return app
