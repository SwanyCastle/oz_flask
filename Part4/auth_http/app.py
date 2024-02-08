from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": "hello",
    "susan": "bye"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

@app.route('/')
def indes():
    return render_template('index.html')

@app.route('/protected')
@auth.login_required
def protected():
    return render_template('secret.html')

if __name__ == "__main__":
    app.run(debug=True)