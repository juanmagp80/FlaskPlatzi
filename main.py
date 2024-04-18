from flask import Flask, request, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu-clave-secreta'

bootstrap = Bootstrap(app)


todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar video a productor']

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)


def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = redirect('/hello')
    response.set_cookie('user_ip', user_ip) 
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    login_form = LoginForm()
    context = {
        'user_ip': user_ip, 
        'todos': todos,
        'login_form': login_form
        
    }
    print(context)
    return render_template('hello.html', **context)

if __name__ == '__main__':
    app.run(debug=True)