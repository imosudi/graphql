from . import app
from .mysqltojson import flatToCascadedJson
import os, json
from flask import jsonify


dbtable = 'patients' #'labtests' # 'transactions' #'user' #'patients'





# Flask Rest & Graphql Routes
@app.route('/')
def hello_world():
    #jsonfile = f'table_json/{dbtable}.json'
    jsonconvert = flatToCascadedJson(dbtable)
    cascaded, flatcopy = jsonconvert.reformatjson()
    #print(cascaded)
    #print(flatcopy)
    #return 'Hello From Graphql Tutorial!'
    #return json.dumps(json.loads(cascaded), indent=4)
    return jsonify(flatcopy)
