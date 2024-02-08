# flash - redirect 하기전에 알려주는 안내메시지를 띄워주는 역할
from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)

# 실제로 배포시에는 .env 또는 yaml 에 따로 저장해서 배포 해야함 github 에 올리면 우리 DB 의 모든 정보가 털릴 수 있음
app.secret_key = 'flask-secret-key' 

# admin user
users = {
    'john': 'pw123',
    'leo': 'pw123'
}

# 메인 페이지
@app.route('/')
def index():
    return render_template("login.html")

# 로그인 요청 오면 처리해주는 API
@app.route('/login', methods=['POST'])
def login():
    # 지금은 request 에서 form 데이터를 받아옴 (json 을 받아 올 수도 있음)
    username = request.form['username']
    password = request.form['password']

    # 지금은 dict 자료형에 있지만 DB 에 값이 저장되어 있다면 
    # 유저가 보낸 데이터가 DB 에 있는지 확인하는 로직
    # 있으면 secret 페이지로 redirect 시켜줌
    if username in users and users[username] == password :
        session['username'] = username
        return redirect('/secret')
    
    # 없으면 메인페이지로 redirect 시켜줌
    flash("Invalid username or password")
    return redirect('/')

@app.route('/secret')
def secret():
    # secret 페이지를 보여주기 전에 해당 유저가 세션이 있는지 확인
    # 예를 들어서 로그인하지 않고 127.0.0.1:5000/secret 으로 직접 접속하려 
    # 할 수도 있기 때문에 secret 페이지를 보여주기 전에 한번더 검사

    # 있으면 secret 페이지 렌더링 해주고
    if 'username' in session:
        return render_template('secret.html')
    # 없으면 메인페이지로 redirect 시켜줌
    return redirect('/')

# 로그아웃
@app.route('/logout')
def logout():
    # 세션에서 현제 유저의 세션 정보를 삭제(pop 이라서 스택에서 꺼내는 느낌) 하고 
    # 메인 페이지로 redirect 시켜줌
    session.pop('username', None)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)