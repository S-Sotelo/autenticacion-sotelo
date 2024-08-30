from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

posts_categories = db.Table(
    'posts_categories',
    db.Column("categories_id", db.Integer, db.ForeignKey('categories.id'), nullable=False, primary_key=True),
    db.Column("posts_id", db.Integer, db.ForeignKey('posts.id'), nullable=False, primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, default="")
    password = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, default=True)
    profile = db.relationship('Profile', backref='users', uselist=False)
    posts = db.relationship('Post', backref='user')


class Profile(db.Model):
    _tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    biography = db.Column(db.String, default="")
    phone = db.Column(db.String, default="")
    github = db.Column(db.String, default="")
    linkedin = db.Column(db.String, default="")
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String, nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    categories = db.relationship('Category', secondary=posts_categories)



class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    posts = db.relationship('Post', secondary=posts_categories)


"""
class PostCategory(db.Model):
    __tablename__ = 'post_categories'
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False, primary_key=True)
    categories_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False, primary_key=True)
"""