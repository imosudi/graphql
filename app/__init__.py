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
from .dbconnect import *

from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

#print(dbhost, dbname, dbuser, pw)

"""# Database Configs [Check it base on other Database Configuration]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True"""

# Database configuration for mysql
app.config['SECRET_KEY'] = 'verydifficult-cashubposweb-secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{dbuser}:{pw}@{dbhost}/{dbname}" .format(dbuser=dbuser, pw=pw, dbhost=dbhost, dbname=dbname)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize Database
db = SQLAlchemy(app)
db.init_app(app)

migrate = Migrate(app, db)


from .models import *
from .graphQLSchema import *
from .graphQLqueryAndmutation import *

from .routes import *

