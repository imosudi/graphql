from graphene_sqlalchemy_filter import FilterSet
 
from model import *
 
ALL_OPERATIONS = ['eq', 'ne', 'like', 'ilike', 'is_null', 'in', 'not_in', 'lt', 'lte', 'gt', 'gte', 'range']
 
 
class UserFilter(FilterSet):
    class Meta:
        model = UserModel
        fields = {
            'userid': ALL_OPERATIONS,
            'name': ALL_OPERATIONS,
            'surname': ALL_OPERATIONS,
            'age': ALL_OPERATIONS,
        }