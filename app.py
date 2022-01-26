import os

import graphene
from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Database Configs [Check it base on other Database Configuration]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Initialize Database
db = SQLAlchemy(app)


# ------------------  Database Models ------------------

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    email = db.Column(db.String(256), index=True, unique=True)  # index => should not be duplicate
    posts = db.relationship('Post', backref='author')

    def __repr__(self):
        return '<User %r>' % self.email


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % self.title


# ------------------ Graphql Schemas ------------------


# Objects Schema
class PostObject(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (graphene.relay.Node,)


class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_posts = SQLAlchemyConnectionField(PostObject)
    all_users = SQLAlchemyConnectionField(UserObject)


# noinspection PyTypeChecker
schema_query = graphene.Schema(query=Query)


# Mutation Objects Schema
class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        email = graphene.String(required=True)

    post = graphene.Field(lambda: PostObject)

    def mutate(self, info, title, body, email):
        user = User.query.filter_by(email=email).first()
        post = Post(title=title, body=body)
        if user is not None:
            post.author = user
        db.session.add(post)
        db.session.commit()
        return CreatePost(post=post)


class Mutation(graphene.ObjectType):
    save_post = CreatePost.Field()


# noinspection PyTypeChecker
schema_mutation = graphene.Schema(query=Query, mutation=Mutation)


# Flask Rest & Graphql Routes
@app.route('/')
def hello_world():
    return 'Hello From Graphql Tutorial!'


# /graphql-query
app.add_url_rule('/graphql-query', view_func=GraphQLView.as_view(
    'graphql-query',
    schema=schema_query, graphiql=True
))

# /graphql-mutation
app.add_url_rule('/graphql-mutation', view_func=GraphQLView.as_view(
    'graphql-mutation',
    schema=schema_mutation, graphiql=True
))

if __name__ == '__main__':
    app.run()