from datetime import datetime, timedelta
#import psycopg2
from flask import Flask
import flask
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/pythonhw'
db = SQLAlchemy(app)

class Account(db.Model):
    __tablename_ = 'account'
    id = db.Column('id', db.Integer, primary_key = True)
    nickname = db.Column('nickname', db.String(50))
    password = db.Column('password' ,db.String(16))
    token = db.Column('token', db.String)

    def __init__(self, nickname, password, token):
        self.nickname = nickname
        self.password = password
        self.token = token


@app.route('/login')
def login():
    
    auth = request.authorization
    if auth:
        nick = Account.query.filter_by(nickname = auth.username).first()
    if auth and auth.password == nick.password:
        token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=1)}, app.config['SECRET_KEY'])
        sub = Account.query.filter_by(nickname = auth.username).first()
        sub.token = token
        db.session.commit()
        return jsonify({'token': token.decode('UTF-8')})
    
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return "<h1>Hello, Token is missing! </h1>"

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return "<h1>Hello, Could not verify the token </h1>"
        return f(*args, **kwargs)
    return decorated

@app.route('/protected')
@token_required
def protected():
    return "<h1>Hello, token which is provided is correct </h1>, "


if __name__ == '__main__':
    app.run(debug=True)
