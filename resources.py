from flask_restful import Resource, reqparse
from models import User
from flask import session, redirect

class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Username is required')
    parser.add_argument('password', type=str, required=True, help='Password is required')
    parser.add_argument('email', type=str, required=True, help='Email is required')

    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if user:
                return user.serialize()
            return {'message': 'User not found'}, 404

        users = User.query.all()
        return [user.serialize() for user in users]

    def post(self):
        data = UserResource.parser.parse_args()
        username = data['username']
        password = data['password']
        email = data['email']

        user = User.query.filter_by(username=username).first()
        if user:
            return {'message': 'User already exists'}, 400

        user = User(username, password, email)
        db.session.add(user)
        db.session.commit()

        return user.serialize(), 201

class LoginResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Username is required')
    parser.add_argument('password', type=str, required=True, help='Password is required')

    def post(self):
        data = LoginResource.parser.parse_args()
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return {'message': 'Invalid credentials'}, 401

        session['user_id'] = user.id

        return {'message': 'Login successful'}, 200
