from datetime import datetime

from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	#第一个参数“多”的模型类，第二个定义将添加到“多”类的对象的字段的名称，第三个参数lazy定义了如何发布对关系的数据库查询
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.forfamat(self.username)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	#user_id列作为user表的外键
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post {}'.format(self.body)