import os
import secrets
from datetime import datetime
from flask import Blueprint, render_template, request, jsonify, current_app
from werkzeug.utils import secure_filename
from app import db
from app.models.munRegistration import MunRegistration
from app import allowed_file
from app.services import user_service

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.post("/register")
def register_user():
    try:
        upload_folder = current_app.config.get("UPLOAD_FOLDER", "app/static/uploads")
        os.makedirs(upload_folder, exist_ok=True)

        if 'paymentSlip' not in request.files:
            return jsonify({'error': 'No payment proof provided'}), 400
            
        payment_slip = request.files['paymentSlip']
        
        if payment_slip.filename == '':
            return jsonify({'error': 'No selected file'}), 400
            
        if not allowed_file(payment_slip.filename):
            return jsonify({'error': 'File type not allowed'}), 400

        filename = secure_filename(f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{payment_slip.filename}")
        filepath = os.path.join(upload_folder, filename)
        payment_slip.save(filepath)

        relative_path = os.path.join('uploads', filename)
        secure_8_digit = secrets.randbelow(90000000) + 10000000

        referrel_code = request.form.get("referedBy")
        referred_by_id = None
        
        if referrel_code: 
            referring_user = MunRegistration.query.filter_by(referral_code=referrel_code).first()
            if not referring_user:
                return jsonify({'error': 'Invalid referral code provided'}), 400
            referred_by_id = referring_user.id
            referring_user.number_of_referral += 1

        first_name = request.form.get('firstName')

        new_participant = MunRegistration(
            first_name=request.form.get('firstName'),
            last_name=request.form.get('lastName'),
            email=request.form.get('email'),
            address=request.form.get('address'),
            dob=datetime.strptime(request.form.get('dob'), '%Y-%m-%d').date(),
            primary_phone=request.form.get('primaryPhone'),
            secondary_phone=request.form.get('secondaryPhone'),
            whatsapp_number=request.form.get('whatsappNumber'),
            food_preference=request.form.get('foodPref'),
            previous_college=request.form.get('prevEnroll'),
            stream=request.form.get('stream'),
            mun_experience=request.form.get('alreadyMun') == 'yes',
            primary_committee=request.form.get('committee'),
            secondary_committee=request.form.get('secondaryCommittee'),
            global_issue_response=request.form.get('globalIssue'),
            future_goals=request.form.get('futureGoal'),
            medical_conditions=request.form.get('medicalCondition'),
            refered_by=referred_by_id, 
            referral_code=f"#{first_name}-{secure_8_digit}",
            payment_proof=relative_path
        )

        db.session.add(new_participant)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': 'Registration successful!',
            'participant_id': new_participant.id
        }), 201

    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Registration error: {str(e)}")
        return jsonify({'error':'An internal error has occurred. Please try again later.'}), 500


@main_bp.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']

    UserService.create_user(username, password)
    return redirect(url_for('main.index'))