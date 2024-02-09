from flask import request, jsonify, abort
from flask_smorest import Blueprint
from flask.views import MethodView

from models import User, Post
from db import db

user_blp = Blueprint("Users", __name__, url_prefix='/users')

@user_blp.route('/')
class UserList(MethodView):
    def get(self):
        users = User.query.all()
        datas = [
            {
                "id": user.id,
                "name": user.name
            } for user in users
        ]
        return jsonify(datas), 200

    def post(self):
        data = request.json
        user = User(name=data['name'])
        db.session.add(user)
        db.session.commit()
        return jsonify({ "msg": "Successfully Add User" }), 201

@user_blp.route('/<string:username>')
class UserResource(MethodView):
    def put(self, username):
        data = request.json
        user = User.query.filter_by(name=username).first()
        if not user:
            abort(404, "User Not Found")
        user.name = data['name']
        db.session.commit()

        return jsonify({ "msg": "Successfully Update User" }), 201

    def delete(self, username):
        user = User.query.filter_by(name=username).first()
        if not user:
            abort(404, "User Not Found")
        db.session.delete(user)
        db.session.commit()

        return jsonify({ "msg": "Successfully Delete User" }), 200

@user_blp.route('/post/<string:username>')
class UserPostResource(MethodView):
    def get(self, username):
        user = User.query.filter_by(name=username).first()
        if not user:
            abort(404, "User Not Found")
        posts = Post.query.filter_by(user_id=user.id)
        datas = [
            {
                "id": post.id,
                "title": post.title,
                "likes": post.likes,
                "user_id": post.user_id
            } for post in posts
        ]
        return jsonify(datas), 200

    def post(self, username):
        data = request.json
        user = User.query.filter_by(name=username).first()
        if not user:
            abort(404, "User Not Found")
        post = Post(title=data['title'], user_id=user.id)
        db.session.add(post)
        db.session.commit()

        return jsonify({ "msg": "Successfully Add Post" }), 201

@user_blp.route('/post/like/<string:username>/<string:title>')
class PostResource(MethodView):
    def post(self, username, title):
        user = User.query.filter_by(name=username).first()
        if not user:
            abort(404, "User Not Found")
        post = Post.query.filter_by(title=title).first()
        if not post:
            abort(404, "Post Not Found")
        post.likes += 1
        db.session.commit()
        
        return jsonify({ "msg": "Successfully Up Likes" }), 201

    def put(self, username, title):
        data = request.json
        user = User.query.filter_by(name=username).first()
        if not user:
            abort(404, "User Not Found")
        post = Post.query.filter_by(title=title).first()
        if not post:
            abort(404, "Post Not Found")
        post.title = data['title']

        db.session.commit()

        return jsonify({ "msg": "Successfully Update Post" }), 201
    
    def delete(self, username, title):
        user = User.query.filter_by(name=username).first()
        if not user:
            abort(404, "User Not Found")
        post = Post.query.filter_by(title=title).first()
        if not post:
            abort(404, "Post Not Found")
        db.session.delete(post)
        db.session.commit()

        return jsonify({ "msg": "Successfully Delete Post "}), 200