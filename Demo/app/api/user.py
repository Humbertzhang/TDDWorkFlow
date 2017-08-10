from . import api
from app import db
from flask import request,jsonify,Response
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
import json

@api.route('/signup/',methods=['POST'])
def signup():
    if request.method == 'POST':
        name = request.get_json().get("username")
        password = request.get_json().get("password")
        if not User.query.filter_by(username=name).first():
            user = User(username=name,
                    password=password)
            db.session.add(user)
            db.session.commit()
            user_id=User.query.filter_by(username=name).first().id
            return jsonify({
                "created":user_id,
            })

@api.route('/signin/', methods=['POST'])
def login():
    email = request.get_json().get("email")
    password = request.get_json().get("password")
    try:
        user = User.query.filter_by(email=email).first()
    except:
        user = None
        uid = None
    if user is not None and user.verify_password(password):
        uid = user.id
        token = user.generate_auth_token()
        return jsonify({
            "uid":user.id,
            "token":token,
        })
