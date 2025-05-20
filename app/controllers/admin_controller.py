import os
from datetime import datetime
from flask import Blueprint, render_template, request, jsonify, current_app, make_response, flash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from app import db
from app.models.munRegistration import MunRegistration
from app.models.user import User
from app import allowed_file

admin_bp = Blueprint('admin', __name__)

@admin_bp.get('/login')
def admin_login():
    return render_template('login.html')

@admin_bp.post("/login")
def admin_login_post():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Please enter both username and password', 'danger')
            return render_template('login.html')

        admin = User.query.filter_by(username=username).first()
        
        if not admin or not admin.check_password(password):
            flash('Invalid username or password', 'danger')
            return render_template('login.html')

        # Update last login
        # admin.last_login = datetime.utcnow()
        # db.session.commit()

        access_token = create_access_token(identity={
            'username': username,
            'role': user['role']
        })

        resp = make_response()
        resp.set_cookie('au_ssid',access_token, 3600,3600,"/")

        flash('Login successful', 'success')
        return redirect(url_for('admin.dashboard'))

    return render_template('login.html')


@admin_bp.get("/dashboard")
def dashboard():
    return render_template('view_registrations.html')