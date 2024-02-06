from flask import Flask
from flask_smorest import Api
from api import blp

app = Flask(__name__)

# flask-smorest 를 사용하게 되면 OpenAPI 및 Swagger 설정을 통해서 API 문서화가 가능
# OpenAPI : 웹 API 를 설명하기 위한 스펙이고 RESTful API 의 설계와 문서화를 위한 표준 형식
#            API 엔드포인트, 리소스, 메서드, 요청 및 응답형식, 인증방법 등 아래 표같은 느낌
#            | Endpoint | HTTP Method   | Description                     | URL Path |
#            | ItemList | GET           | 모든 아이템을 반환                   | /items/ |
#            | ItemList | POST          | 새 아이템을 추가                     | /items/ |
#            | Item     | GET           | 특정 ID를 가진 아이템을 반환           | /items/<int:item_id> |
#            | Item     | PUT           | 특정 ID를 가진 아이템을 업데이트        | /items/<int:item_id> |
#            | Item     | DELETE        | 특정 ID를 가진 아이템을 삭제           | /items/<int:item_id> |
# OpenAPI 및 Swagger 설정
app.config["API_TITLE"] = "Book API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
# flask-smorest 블루프린트 등록
api.register_blueprint(blp)
