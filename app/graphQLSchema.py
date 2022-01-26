from .import app
from .graphQLqueryAndmutation import *
from flask_graphql import GraphQLView



# /graphql-query
app.add_url_rule('/graphql-query', view_func=GraphQLView.as_view(
    'graphql_query',
    schema=schema_query, graphiql=True
))

# /graphql-mutation
app.add_url_rule('/graphql-mutation', view_func=GraphQLView.as_view(
    'graphql_mutation',
    schema=schema_mutation, graphiql=True
))