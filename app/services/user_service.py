from app.models import User
from app import db
from app.models.user import User

class UserService:
    @staticmethod
    def create_user(username, password):
        hashPassword = User.set_password(password=password)
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
