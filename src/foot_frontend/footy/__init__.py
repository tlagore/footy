from flask import Flask
from flask_pymongo import PyMongo
from footy_auth.footy_auth import AppKeyManager

key_manager = AppKeyManager()

footy_app = Flask(__name__)
footy_app.config["MONGO_URI"] = key_manager.get_secret("MongoDBConnectionString")
mongo = PyMongo(footy_app)

from footy import routes
