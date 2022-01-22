from . import app

# Flask Rest & Graphql Routes
@app.route('/')
def hello_world():
    return 'Hello From Graphql Tutorial!'