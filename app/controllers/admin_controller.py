import os
from datetime import datetime
from flask import Blueprint, render_template, request, jsonify, current_app
from werkzeug.utils import secure_filename
from app import db
from app.models.munRegistration import MunRegistration
from app import allowed_file

admin_bp = Blueprint('admin', __name__)

@admin_bp.get('/login')
def admin_login():
    return render_template('login.html')

@admin_bp.get("/dashboard")
def dashboard():
    return render_template('view_registrations.html')