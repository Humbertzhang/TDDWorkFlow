import unittest
from app import create_app
from flask import current_app, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import json
import base64

db = SQLAlchemy()
number = random.randint(1,9999)

class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exist(self):
        self.assertFalse(current_app is None)
        
    #Test Register
    def test_a_signup(self):
        response = self.client.post(
                url_for('api.signup',_external=True),
                data = json.dumps({
                        "username":str(number),
                        "password":str(number)
                    }),
                content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    #Test Login
    def test_b_signin(self):
        response = self.client.post(
                url_for('api.signin',_external=True),
                data = json.dumps({
                        "username":str(number),
                        "password":str(number)
                    }),
                content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
        
        token = json.loads(response.data)['token']
        global B64TOKEN
        B64TOKEN = str(base64.b64encode(token))
        
    #Test GET 
    def test_c_getname(self):
        response = self.client.get(
            url_for('api.getname',_external=True),
            headers = { "Authorization":"Basic" + B64TOKEN},
            content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    #Test POST
    def test_c_changename(self):
        response = self.client.put(
            url_for('api.changename',_external=True),
            headers = { "Authorization":"Basic" + B64TOKEN},
            data = json.dumps({
                "username":str(number*2)
            }),
            content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
