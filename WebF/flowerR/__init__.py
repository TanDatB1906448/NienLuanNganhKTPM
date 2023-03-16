from flask import Flask, request, Blueprint
from .FRModel.controller import FGModel
from .views import views

def createApp(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    # print(app.config)
    app.register_blueprint(FGModel)
    app.register_blueprint(views)
    return app