
# ------------------ Graphql Schemas ------------------
import os

import graphene
from flask import Flask, config
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField


from .import db 
from .models import *


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
