from flask import Flask, render_template
from flask_smorest import Api
from flask_migrate import Migrate

from db import db
from models import Post
from routes.posts import post_blp

import yaml

app = Flask(__name__)

mysql_uri = ""
with open("key.yaml", "r") as f:
    key = yaml.load(f, Loader=yaml.FullLoader)
    mysql_uri = key["mysql_uri"]

app.config["SQLALCHEMY_DATABASE_URI"] = mysql_uri
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
api.register_blueprint(post_blp)

@app.route("/manage-posts")
def manage_posts():
    return render_template('posts.html')


if __name__ == "__main__":
    with app.app_context():
        # models.py 에 정의한 User, Board 클래스가 테이블로 만들어짐
        db.create_all()

    app.run(debug=True)