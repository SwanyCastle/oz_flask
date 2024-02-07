from flask_smorest import Blueprint
from flask import request, jsonify
from flask.views import MethodView
from db import db
from models import Post

post_blp = Blueprint('Posts', 'posts', description='Operations on Posts', url_prefix='/posts')

@post_blp.route('/')
class PostList(MethodView):
    def get(self):
        posts = Post.query.all()
        
        return jsonify([
            {
                "id": post.id, 
                "title": post.title, 
                "content": post.content,
                "created_at": post.created_at
            } for post in posts
        ])
    
    def post(self):
        data = request.json
        new_post = Post(title=data['title'], content=data['content'])
        db.session.add(new_post)
        db.session.commit()

        return jsonify({'msg': 'success create post'}), 201


@post_blp.route('/<int:post_id>')
class PostResource(MethodView):
    def get(self, post_id):
        post  = Post.query.get_or_404(post_id)
        
        return jsonify(
            {
                "id": post.id, 
                "title": post.title, 
                "content": post.content,
                "created_at": post.created_at
            }
        )

    def put(self, post_id):
        post = Post.query.get_or_404(post_id)
        data = request.json

        post.title = data['title']
        post.content = data['content']

        db.session.commit()

        return jsonify({"msg": "successfully update post data"}), 201

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return jsonify({"msg": "successfully delete post data"}), 200
        # return jsonify({"msg": "successfully delete post data"}), 204 -> 204 로 내려주면 postman 에 msg 표시 안됨
