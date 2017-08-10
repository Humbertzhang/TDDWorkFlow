from . import api
from app import db
from flask import request,jsonify,Response
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
import json

@api.route('/signup/',methods=['GET','POST'])
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
