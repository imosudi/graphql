import os, time
from os.path import join, dirname
from dotenv import load_dotenv
from flask import jsonify
import json

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


### SQLAlchemy config
#dbhost="mio1.serverafrica.net"
dbhost	= os.environ.get("DB_HOST") 
dbname	= os.environ.get("DB_NAME") 
dbuser	= os.environ.get("DB_USER") 
pw	= os.environ.get("DB_PASS")