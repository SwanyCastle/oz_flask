from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import User

user_blp = Blueprint('Users', 'users', description="Operations on users", url_prefix="/user")

@user_blp.route('/')
class UserList(MethodView):
    # 1. 전체 유저 데이터 조회 (GET)
    def get(self):
        users = User.query.all()

        users_data = [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
            for user in users
        ]

        return jsonify(users_data)

    # 2. 유저 등록 (POST)
    def post(self):
        data = request.json
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "Successfully Created User"}), 201

@user_blp.route('/<int:user_id>')
class UserResource(MethodView):
    # 1. 특정 유저 데이터 조회 (GET)
    def get(self, user_id):
        user = User.query.get_or_404(user_id)

        return jsonify({
            "name": user.name,
            "email": user.email
        })

    # 2. 특정 유저 데이터 업데이트 (PUT)
    def put(self, user_id):
        data = request.json
        user = User.query.get_or_404(user_id)
        user.name = data['name']
        user.email = data['email']

        db.session.commit()

        return jsonify({"msg": "Successfully Updated User"}), 201

    # 3. 특정 유저 데이터 삭제 (DELETE)
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"msg": "Successfully Deleted User"}), 200
        # return jsonify({"msg": "Successfully Deleted User"}), 204 -> 204 로 내려주면 postman 에 msg 표시 안됨
