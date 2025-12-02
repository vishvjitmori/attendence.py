from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'Your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.model import User

    @app.context_processor
    def inject_user():
        user = None
        if 'user_id' in session:
            user = User.query.get(session['user_id'])
        return {'current_user': user}

    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.addstore import addstore_bp
    from app.routes.storelist import storelist_bp
    from app.routes.employeelist import employeelist_bp
    from app.routes.addemployee import addemployee_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(addstore_bp)
    app.register_blueprint(storelist_bp)
    app.register_blueprint(employeelist_bp)
    app.register_blueprint(addemployee_bp)

    return app