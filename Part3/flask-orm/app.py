from flask import Flask, render_template
from flask_smorest import Api
from db import db
from models import User, Board
from routes.boards import board_blp
from routes.users import user_blp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/oz"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# blueprint 설정
app.config["API_TITLE"] = "ORM API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(board_blp)
api.register_blueprint(user_blp)

@app.route("/manage-boards")
def manage_boards():
    return render_template('boards.html')

@app.route("/manage-users")
def manage_users():
    return render_template('users.html')

if __name__ == "__main__":
    with app.app_context():
        # models.py 에 정의한 User, Board 클래스가 테이블로 만들어짐
        db.create_all()

    app.run(debug=True)