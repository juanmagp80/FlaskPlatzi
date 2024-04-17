from flask import Flask, request, Response, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index ():
    user_ip= request.remote_addr
    response = make_response = (redirect('/hello'))
    response.set_cookie('user_ip', user_ip) 
    return response
@app.route('/hello')
def hello ():
    user_ip = request.cookies.get('user_ip')

    user_ip= request.remote_addr
    return render_template('hello.html', user_ip=user_ip)

if __name__ == '__main__':
    app.run(debug=True)