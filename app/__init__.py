from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Inisialisasi ekstensi
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.secret_key = '05df6d4dd8880f8e78692866854a4a2de08f6afb9be4ef6a'
    app.config.from_object('app.config.Config')

    # Inisialisasi ekstensi dengan aplikasi Flask
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Daftarkan blueprint
    from app.routes import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
