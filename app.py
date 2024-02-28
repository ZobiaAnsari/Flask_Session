from flask import Flask, request, session
from datetime import timedelta

app=Flask(__name__)
app.secret_key='hello'
app.permanent_session_lifetime = timedelta(seconds=5)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        username = request.json['username']
        password = request.json['password']
        session['username'] = username

        if username == 'zobia' and password == 1234:
            return 'logged in '
        else:
            return ("invalid credentials")
    else:
        if 'user' in session:
            return 'Login success'
    
@app.route('/user')
def user():
    if 'username' in session:
        username = session['username']
        return f'{username}  Page Accessed'
    else:
        return "Require Log-in Session Id expire"
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return ("logout success")


if __name__ == '__main__':

    app.run(debug=True)

