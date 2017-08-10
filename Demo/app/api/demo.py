from . import api
from guisheng_app import db
from flask import request,jsonify,Response
from flask_login import login_user, logout_user, current_user, login_required
from guisheng_app.models import User
from guisheng_app.decorators import admin_required
import json

@api.route('/getname/<int:id>',methods=['GET'])
