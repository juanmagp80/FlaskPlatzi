from flask_testing import TestCase
from main import app
from flask import current_app
from flask import url_for
from flask import request
from app.forms import LoginForm

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)
        
    def test_app_in_testing_mode(self):
        self.assertTrue(current_app.config['TESTING'])
        
    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))
        
    def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response)        
        
    def test_hello_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('hello'), data=fake_form)W
        self.assertTrue(response, status_code, 405)
        
    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)
        
    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))
        self.assert200(response)
    
    def test_auth_login_template(self):
        
       response = self.client.get(url_for('auth.login'))
       self.assertTemplateUsed(response, 'login.html')
        