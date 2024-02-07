# Model 생성 --> Table 생성
# 게시글 - board
# 유저 - user

from db import db

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    # 역참조 ->  ex) 사용자 A 가 작성한 게시글 모두 불러와줘 할 때 사용
    # SQLAlchemy 에서는 관계를 나타내는 쿼리셋을 반환 하는데 쿼리셋은 DB 로부터 즉시 모든 데이터를
    # 로딩하지 않고 필요할 때 해당 쿼리를 실행해서 데이터를 로드하는 것 lazy='dynamic' 
    boards = db.relationship("Board", back_populates='author', lazy='dynamic')

class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    # 게시글과 유저를 연결 해주는 외래키 (user.id)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # 역참조 ->  ex) 사용자 A 가 작성한 게시글 모두 불러와줘 할 때 사용
    author = db.relationship('User', back_populates="boards")