from . import api
from app import db
from flask import request,jsonify,Response
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
import json

@api.route('/getname/<int:id>',methods=['GET'])
def getname(id):
    if request.method == 'GET':
        uid = id
        if User.query.filter_by(id=uid).first():
            user = User.query.filter_by(id=uid).first()
            return jsonify({
                        "username":user.username
                    })
