from flask import Flask
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(__file__).resolve().parent.parent/'.env')
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']=os.getenv('SECRET_KEY','change-this-in-production')
    from .routes.main import main_bp
    app.register_blueprint(main_bp)
    return app
