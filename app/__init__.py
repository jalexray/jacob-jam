import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

from flask import Flask, request, current_app
from flask_bootstrap import Bootstrap
from config import Config

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	from app.errors import bp as errors_bp  # errors v 0.0
	app.register_blueprint(errors_bp)

	from app.main import bp as main_bp  # main v 0.0
	app.register_blueprint(main_bp)

	return app
