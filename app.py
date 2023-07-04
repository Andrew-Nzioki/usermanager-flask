from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_session import Session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'your_secret_key'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
api = Api(app)
migrate = Migrate(app, db)
Session(app)

from resources import UserResource, LoginResource
from views import protected_page, home

api.add_resource(UserResource, '/users', '/users/<int:user_id>')
api.add_resource(LoginResource, '/login')

app.add_url_rule('/protected-page', 'protected_page', protected_page)
app.add_url_rule('/', 'home', home)

if __name__ == '__main__':
    app.run(debug=True)
