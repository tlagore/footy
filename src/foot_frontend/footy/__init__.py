from flask import Flask

footy_app = Flask(__name__)

from footy import routes
