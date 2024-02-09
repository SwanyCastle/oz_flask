from flask_migrate import Migrate

from db import db

import yaml

def app_configure(app):
    mysql_uri = ""
    with open('key.yaml', 'r') as f:
        key = yaml.load(f, Loader=yaml.FullLoader)
        mysql_uri = key['mysql_uri']

    app.config["SQLALCHEMY_DATABASE_URI"] = mysql_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    migrate = Migrate(app, db)

    app.config["API_TITLE"] = "ORM API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.1.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

