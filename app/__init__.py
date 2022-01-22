"""
Workaround import error
pip install graphql-core==2.2.1
pip install graphene==2.1.8
"""
import os

import graphene
from flask import Flask, config
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

import config


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Database Configs [Check it base on other Database Configuration]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Initialize Database
db = SQLAlchemy(app)

from .models import *
from .graphQLSchema import *
from .graphQLqueryAndmutation import *

# Flask Rest & Graphql Routes
@app.route('/')
def hello_world():
    return 'Hello From Graphql Tutorial!'

