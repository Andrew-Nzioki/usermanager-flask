from flask import render_template, session
from models import User

def protected_page():
    user_id = session.get('user_id')
    if not user_id:
        return {'message': 'Not authenticated'}, 401

    user = User.query.get(user_id)
    if not user:
        return {'message': 'User not found'}, 404

    return {'message': f'Welcome, {user.username}!'}

def home():
    return render_template('home.html')
