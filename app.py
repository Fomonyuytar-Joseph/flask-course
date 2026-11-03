from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from  flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://joe:123@localhost:5432/test_db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'

    db.init_app(app)

    from routes import register_routes

    register_routes(app , db)

    migrate = Migrate(app, db)
    return app
