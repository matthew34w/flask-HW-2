from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():


        from .auth import auth
        from .cars import cars

        app.register_blueprint(auth)
        app.register_blueprint(cars)
    
    return app


