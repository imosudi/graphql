from graphene_sqlalchemy_filter import FilterSet
 
from app.models import *


 
ALL_OPERATIONS = ['eq', 'ne', 'like', 'ilike', 'is_null', 'in', 'not_in', 'lt', 'lte', 'gt', 'gte', 'range']
class PatientFilter(FilterSet):
    class Meta:
        model = Patients
        fields = {
            'patient_id': ALL_OPERATIONS,
            'patientSex': ALL_OPERATIONS,
            'patientPhonenumber': ALL_OPERATIONS,
            'patientID': ALL_OPERATIONS,
            'ageGrade': ALL_OPERATIONS,
        }

class LabtestFilter(FilterSet):
    class Meta:
        model = Labtests
        fields = {
            'test_id ': ALL_OPERATIONS,
            'testName': ALL_OPERATIONS,
            'testType': ALL_OPERATIONS,
            'testmnemonics': ALL_OPERATIONS,
        }

class TransactionFilter(FilterSet):
    class Meta:
        model = Transactions
        fields = {
            'transactionId': ALL_OPERATIONS,
            'CurrentpatientID': ALL_OPERATIONS,
            'barcode': ALL_OPERATIONS,
            'billto': ALL_OPERATIONS,
            'fullName': ALL_OPERATIONS,
            'subtotal': ALL_OPERATIONS,
            'total': ALL_OPERATIONS,
            'payment': ALL_OPERATIONS,
            'paymentmethod': ALL_OPERATIONS,
            'transactTime': ALL_OPERATIONS,
            'cashier': ALL_OPERATIONS,
        }

           
    