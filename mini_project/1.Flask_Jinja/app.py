from flask import Flask

from routes.users import routing_app
from config import app_configure
from db import db

app = Flask(__name__)

app_configure(app)
routing_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)