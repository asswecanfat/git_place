from flask import Flask
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_sqlalchemy import SQLAlchemy

from ..all_config import config

db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)


def creat_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    configure_uploads(app, photos)
    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
