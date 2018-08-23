

from app.app import Flask


def register_blueprints(app):
    from app.api.v1 import create_api_v1
    app.register_blueprint(create_api_v1(),url_prefix='/v1')


def linesql(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()





def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.settings')
    register_blueprints(app)
    linesql(app)

    return app