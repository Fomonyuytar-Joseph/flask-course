from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from  flask_login import LoginManager
from flask_bcrypt import Bcrypt
from models import User


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://joe:123@localhost:5432/test_db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'

    app.secret_key = 'SOME KEY'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    from routes import register_routes

    register_routes(app, db, bcrypt=Bcrypt)

    migrate = Migrate(app, db)
    return app
