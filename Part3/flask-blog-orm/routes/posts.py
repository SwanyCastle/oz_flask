from flask_smorest import Blueprint
from flask import request, jsonify
from flask.views import MethodView
from db import db
from models import Post

from datetime import datetime
import pytz

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
                "created_at": post.created_at,
                "updated_at": post.updated_at
            } for post in posts
        ])
    
    def post(self):
        data = request.json
        localtime = pytz.timezone('Asia/Seoul')
        new_post = Post(title=data['title'], content=data['content'], created_at=datetime.now(localtime))
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
                "created_at": post.created_at,
                "updated_at": post.updated_at
            }
        )

    def put(self, post_id):
        post = Post.query.get_or_404(post_id)
        data = request.json
        localtime = pytz.timezone('Asia/Seoul')

        post.title = data['title']
        post.content = data['content']
        post.updated_at = datetime.now(localtime)

        db.session.commit()

        return jsonify({"msg": "successfully update post data"}), 201

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return jsonify({"msg": "successfully delete post data"}), 200
