from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def home():
    return "hello, this is main page!"

@app.route('/about')
def about():
    return "this is the about page!"

# 동적 URL 파라미터 값을 받아서 처리해줌
# http://127.0.0.1:5000/user/seunghwan
@app.route('/user/<username>')
def user(username):
    return f"UserName : { username }"

# POST 요청 날리는 법
# 1 - postman
# 2 - requests

import requests

@app.route('/test')
def test():
    url = "http://127.0.0.1:5000"
    data = 'test data'
    response = requests.post(url=url, data=data)
    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)
    if request.method == 'GET':
        print("&&& GET method &&&", request.data)
    if request.method == 'POST':
        print("*** POST method ***", request.data)
    
    return Response("Successflly submitted", status=200)