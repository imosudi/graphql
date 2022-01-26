from .import app
from .graphQLqueryAndmutation import *

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