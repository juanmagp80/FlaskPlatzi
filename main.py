from flask import Flask, request, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask import session
from flask import url_for
from flask import flash
import unittest
from app import create_app
from app.forms import LoginForm
from flask import make_response
from app.firestore_service import get_users


app = create_app()
app.config['SECRET_KEY'] = 'SUPER SECRETO'


todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar video a productor']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.cli.command()
def test (): 
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response

@app.route('/hello', methods=['GET', 'POST'])
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    user_ip = request.cookies.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip': user_ip, 
        'todos': todos,
        'login_form': login_form,
        'username': username
        
    }
    users = get_users()
    for user in users:
        print(user.id)
        print(user.to_dict())
    #if login_form.validate_on_submit():
        #username = login_form.username.data
       # session['username'] = username
        #flash('Nombre de usuario registrado con éxito')
        
        #return redirect(url_for('index'))
    
    return render_template('hello.html', **context)

if __name__ == '__main__':
    app.run(debug=True)