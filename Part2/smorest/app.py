from flask import Flask
from flask_smorest import Api
from api import blp

app = Flask(__name__)

# flask-smorest 를 사용하게 되면 OpenAPI 및 Swagger 설정을 통해서 API 문서화가 가능
# OpenAPI 및 Swagger 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(blp)