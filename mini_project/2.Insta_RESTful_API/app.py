from flask import Flask, render_template
from flask_smorest import Api
from flask_migrate import Migrate

from db import db
from models import User, Post
from routes.users import user_blp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/insta"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

# blueprint 설정
app.config["API_TITLE"] = "ORM API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(user_blp)

if __name__ == "__main__":
    with app.app_context():
        # models.py 에 정의한 User, Board 클래스가 테이블로 만들어짐
        db.create_all()

    app.run(debug=True)