from flask import render_template
from . import auth
from app.forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login ():
    context = {
        'login_form': LoginForm()
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('Nombre de usuario registrado con éxito')
        
    return render_template('login.html', **context)