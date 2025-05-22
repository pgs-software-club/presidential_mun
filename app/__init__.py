import os 
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg",'jpeg'}

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['UPLOAD_FOLDER'] = os.path.join('app','static', 'uploads')
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

    db.init_app(app)
    migrate.init_app(app, db)

    from app.controllers.index_controller import main_bp
    from app.controllers.admin_controller import admin_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    # with app.app_context():
    #         db.create_all() 
            
    return app

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']