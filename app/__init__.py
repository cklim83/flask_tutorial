from flask import Flask
from config import Config

my_app = Flask(__name__)
my_app.config.from_object(Config)

from app import routes
