from flask import Flask, request, Blueprint
from .FRModel.controller import FGModel
from .Flower.controller import Flowers
from .views import views
from .extensions import ma, db

def createApp(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    ma.__init__(app)
    app.register_blueprint(FGModel)
    app.register_blueprint(views)
    app.register_blueprint(Flowers)
    return app