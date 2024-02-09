from db import db

class User(db.Model):
    __tablename__ = "users_info"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    posts = db.relationship("Post", back_populates='author', lazy='dynamic')

class Post(db.Model):
    __tablename__ = "posts_info"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    likes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("users_info.id"), nullable=False)
    author = db.relationship('User', back_populates="posts")