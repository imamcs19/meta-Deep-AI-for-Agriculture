# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# import os

# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "db/database.db"))

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = database_file
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# from app.controller.AppController import *
