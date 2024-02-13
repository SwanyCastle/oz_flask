from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from db import db, migrate

app = Flask(__name__)

app.debug = True

# Database, JWT 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['API_TITLE'] = 'Todo API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.2'

# db, migrate 설정
db.init_app(app)
migrate.init_app(app, db)

jwt = JWTManager(app)
api = Api(app)

# 모델 및 리소스 불러오기
from models import User, Todo
from routes.auth import auth_blp
from routes.todo import todo_blp

# API에 Blueprint 등록
api.register_blueprint(auth_blp)
api.register_blueprint(todo_blp)

@app.route('/')
def index():
    return render_template('index.html')
