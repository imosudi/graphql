import os, time
from os.path import join, dirname
from dotenv import load_dotenv
from flask import jsonify
import json

from sqlalchemy import create_engine, inspect

import decimal, datetime

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


### SQLAlchemy config
#dbhost="mio1.serverafrica.net"
dbhost	= os.environ.get("DB_HOST") 
dbname	= os.environ.get("DB_NAME") 
dbuser	= os.environ.get("DB_USER") 
pw	= os.environ.get("DB_PASS")


# create sqlalchemy engine
#try:
engine = create_engine("mysql+pymysql://{dbuser}:{pw}@{dbhost}/{db}" 
     .format(dbuser=dbuser, 
            pw=pw, 
            dbhost=dbhost,
            db=dbname))
'''except :
    print('database connection erroe')
    pass'''


def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    # tat = int(invoicetatlist[i])
    # result_time = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.now() + timedelta(hours=tat))
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)  
