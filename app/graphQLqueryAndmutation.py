
# ------------------ Graphql Schemas ------------------
from distutils.log import error
from email import message
##from email import message
from enum import unique
##from ftplib import error_perm
import os
##from pyexpat import model
from sre_constants import SUCCESS
#from typing_extensions import Required

import graphene
##from flask import Flask, config
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

#from pymysql import IntegrityError
from sqlalchemy.exc import IntegrityError

from .import db 
from .models import *

# Objects Schema
class PostObject(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (graphene.relay.Node,)

class PatientObject(SQLAlchemyObjectType):
    class Meta:
        model = Patients
        interfaces = (graphene.relay.Node,)

class LabtestObject(SQLAlchemyObjectType):
    class Meta:
        model = Labtests
        interfaces = (graphene.relay.Node,)

class TransactionObject(SQLAlchemyObjectType):
    class Meta:
        model = Transactions
        interfaces = (graphene.relay.Node,)

class RoleObject(SQLAlchemyObjectType):
    class Meta:
        model = Role
        interfaces = (graphene.relay.Node,)

class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_posts       = SQLAlchemyConnectionField(PostObject)
    all_users       = SQLAlchemyConnectionField(UserObject)
    all_patients    = SQLAlchemyConnectionField(PatientObject)
    all_labtests    = SQLAlchemyConnectionField(LabtestObject)
    all_transactions= SQLAlchemyConnectionField(TransactionObject)
    all_roles       = SQLAlchemyConnectionField(RoleObject)


# noinspection PyTypeChecker
schema_query = graphene.Schema(query=Query)


# Mutation Objects Schema
class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        email = graphene.String(required=True)

    post = graphene.Field(lambda: PostObject)

    def mutate(self, info, title, body, email):
        user = User.query.filter_by(email=email).first()
        post = Post(title=title, body=body)
        if user is not None:
            post.author = user
        db.session.add(post)
        db.session.commit()
        return CreatePost(post=post)

'''class Mutation(graphene.ObjectType):
    save_post = CreatePost.Field()'''

class PatientEnrol(graphene.Mutation):
    error = graphene.String()
    message = graphene.String()
    success = graphene.Boolean()

    class Arguments:
        patientFirstname		= graphene.String(required=True)
        patientLastname			= graphene.String(required=True)
        patientMiddlename		= graphene.String()
        patientSex				= graphene.String(required=True)
        patientTitle			= graphene.String(required=True)
        ageGrade				= graphene.String(required=True)
        patientStatus			= graphene.String(required=True)
        patientType			    = graphene.String(required=True)
        patientID				= graphene.String(required=True)#, unique=True)	
        patientEmail			= graphene.String(required=True)#, unique=True)#, unique=True)
        patientPhonenumber		= graphene.String(required=True)#, unique=True) #, unique=True)
        patientwhatsappnumber	= graphene.String(required=True)        
        patientAddress			= graphene.String(required=True)
        patientCity			    = graphene.String(required=True)
        patientState			= graphene.String(required=True)
        patientCountry			= graphene.String(required=True)
        patientpersonalEnroledby		= graphene.String(required=True)
    
    #new_patient= graphene.Field(lambda: PateintObject)
    patient = graphene.Field(lambda: PatientObject)

    @classmethod
    def mutate(cls, __, info, patientFirstname,
         patientLastname, patientMiddlename,
           patientSex,  patientTitle,  ageGrade, 
            patientStatus, patientType, 
           patientID, patientEmail, patientPhonenumber, 
           patientwhatsappnumber,   patientAddress,   patientCity,  
           patientState,    patientCountry, patientpersonalEnroledby):
        #patient = Patients.query.filter_by(patientID=patientID).first()  patientDateofBirth,      

        try:
            new_patient = Patients(patientFirstname		=  patientFirstname,
                patientLastname		=  patientLastname ,
                patientMiddlename	=  patientMiddlename ,
                patientSex			=  patientSex ,
                patientTitle		=  patientTitle ,
                ageGrade			=  ageGrade ,
                patientStatus		=  patientStatus ,
                patientType			=  patientType ,
                patientID			=  patientID ,
                patientEmail		=  patientEmail ,
                patientPhonenumber	=  patientPhonenumber ,
                patientWhatsappnumber	=  patientwhatsappnumber ,
                patientAddress		=  patientAddress,
                patientCity			=  patientCity,
                patientState		=  patientState ,
                patientCountry		=  patientCountry ,
                patientpersonalEnroledby		=   patientpersonalEnroledby)
            db.session.add(new_patient)
            db.session.commit()
        except IntegrityError as e:
            return PatientEnrol(error=f'{e.orig}')
        return PatientEnrol(success = True, message=f'{patientLastname} {patientFirstname} with ID : {patientID}')
        
'''class Mutation(graphene.ObjectType):
    save_patient = PatientEnrol.Field()'''   


class TransactionAdd(graphene.Mutation):
    error = graphene.String()
    message = graphene.String()
    success = graphene.Boolean()

    class Arguments:
        transaction_id 		= graphene.Int()
        CurrentpatientID 	=  graphene.String(required=True)
        barcode 			=  graphene.String(required=True)
        fullName	 		=  graphene.String(required=True)
        regtype	 		    =  graphene.String(required=True)
        sex	 		        =  graphene.String(required=True)
        billto	 		    =  graphene.String(required=True)
        testspriority	 	=  graphene.String(required=True)
        testscheduletype	=  graphene.String(required=True)
        
        subtotal			=  graphene.String(required=True)
        discount			=  graphene.String(required=True)
        equalltax			=  graphene.String(required=True)
        total	 		    =  graphene.String(required=True)
        
        paymentmethod 		=  graphene.String(required=True)
        payment		 	    =  graphene.String(required=True)
        referenceOrchange	=  graphene.String(required=True)
        sessionconfirm		=  graphene.String(required=True)
        paymentconfirm		=  graphene.String(required=True)
        cashier			    =  graphene.String(required=True)
        #barcode			=  graphene.String(required=True) # Column Duplication
        
        invoicemnemonics		=  graphene.String(required=True)
        invoicetestname		    =  graphene.String(required=True)
        invoiceprice		    =  graphene.String(required=True)
        invoicetat			    =  graphene.String(required=True)
        
        transactTime		    =  graphene.DateTime() #db.Column(db.DateTime, server_default=db.func.now())
        phlebotomy_processed	=  graphene.Boolean() #db.Column(db.Boolean(), default=False) 
        paymentupdateamount	    =  graphene.String(required=True)
        paymentupdateby		    =  graphene.String(required=True)
        paymentupdateTime		=  graphene.DateTime() # db.Column(db.DateTime, server_default=None) # nullable=False),
    
    transaction = graphene.Field(lambda: TransactionObject)
    
    @classmethod
    def mutate(cls, __, info, transaction_id, CurrentpatientID, barcode,
            fullName, regtype,  sex, billto, testspriority, testscheduletype,
            subtotal, discount, equalltax, total, paymentmethod, payment,
            referenceOrchange, sessionconfirm, paymentconfirm, cashier,
            invoicemnemonics, invoicetestname, invoiceprice, invoicetat,
            transactTime, phlebotomy_processed, paymentupdateamount,
            paymentupdateby, paymentupdateTime) :
        try:
            new_transaction = Transactions(transaction_id = transaction_id, CurrentpatientID =  CurrentpatientID,
                                        barcode =   barcode, fullName =  fullName, regtype =  regtype, sex = sex,
                                        billto =   billto,  testspriority =  testspriority, testscheduletype =  testscheduletype,
                                        subtotal =  subtotal, discount =  discount,  ualltax = equalltax, total =  total,
                                        paymentmethod = paymentmethod, payment =   payment, referenceOrchange = referenceOrchange,
                                        sessionconfirm	 =  sessionconfirm, paymentconfirm	 =  paymentconfirm, cashier = cashier,
                                        invoicemnemonics =  invoicemnemonics, invoicetestname =  invoicetestname, invoiceprice =  invoiceprice,
                                        invoicetat = invoicetat, transactTime = transactTime, phlebotomy_processed = phlebotomy_processed,  
                                        paymentupdateamount = 	paymentupdateamount, paymentupdateby =   paymentupdateby,
                                         paymentupdateTime =  paymentupdateTime)
        except IntegrityError as e:
            return TransactionAdd(error=f'{e.orig}')
        return TransactionAdd(success=True, message=f'Labsession Complete, you may print invoice/receipt for {barcode}')

'''class Mutation(graphene.ObjectType):
    save_transaction = TransactionAdd.Field() '''  



class LabtestAdd(graphene.Mutation):
    error = graphene.String()
    message = graphene.String()
    success_msg = graphene.Boolean()
    
    class Arguments:
        #test_id 		    = graphene.Int()
        testType	 		= graphene.String(required=True) # CLINICAL_CHEMISTRY, ENDOSEROLOGY, HAEMATOLOGY, MICROBIOLOGY, SEROLOGY
        testBottleType		= graphene.String(required=True)
        testName	 		= graphene.String(required=True)
        testmnemonics 		= graphene.String(required=True)
        testDetails	 	    = graphene.String()
        testTAT			    = graphene.String(required=True)
        testPrice			= graphene.String(required=True) 
    
    labtest = graphene.Field(lambda: LabtestObject)
    
    @classmethod
    def mutate(cls, __, info, testType, testBottleType, testName,  testmnemonics, testDetails, testTAT, testPrice):
        #labtest = Labtests.query.filter_by(testmnemonics=testmnemonics).first() 

        try:
            new_test = Labtests( testType = testType, testBottleType = testBottleType,
             testName = testName, testmnemonics = testmnemonics, testDetails = testDetails, 
             testTAT = testTAT,  testPrice = testPrice)
            db.session.add(new_test)
            db.session.commit()
        except IntegrityError as e:
            return LabtestAdd(error=f'{e.orig}')
        return LabtestAdd(success_msg = True, message=f'test added to lab store')
   
class Mutation(graphene.ObjectType):
    save_transaction = TransactionAdd.Field() 
    save_labtest = LabtestAdd.Field()
    save_patient = PatientEnrol.Field()
    save_post = CreatePost.Field()


# noinspection PyTypeChecker
schema_mutation = graphene.Schema(query=Query, mutation=Mutation)
