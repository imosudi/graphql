
# ------------------ Graphql Schemas ------------------
from distutils.log import error
from email import message
from ftplib import error_perm
import os
from sre_constants import SUCCESS

import graphene
from flask import Flask, config
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


class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_posts = SQLAlchemyConnectionField(PostObject)
    all_users = SQLAlchemyConnectionField(UserObject)


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
        patientID				= db.Column(db.String(100), unique=True)	
        patientEmail			= graphene.String(required=True)#, unique=True)
        patientPhonenumber		= graphene.String(required=True) #, unique=True)
        patientwhatsappnumber	= graphene.String(required=True)
        
        patientAddress			= graphene.String(required=True)
        patientCity			    = graphene.String(required=True)
        patientState			= graphene.String(required=True)
        patientCountry			= graphene.String(required=True)
        patientpersonalEnroledby		= graphene.String(required=True)
    
    #new_patient= graphene.Field(lambda: PateintObject)

    @classmethod
    def mutate(cls, __, info, patientFirstname,
         patientLastname, patientMiddlename,
           patientSex,  patientTitle,  ageGrade, 
           patientDateofBirth, patientStatus, patientType, 
           patientID, patientEmail, patientPhonenumber, 
           patientwhatsappnumber,   patientAddress,   patientCity,  
           patientState,    patientCountry, patientpersonalEnroledby):
        patient = Patients.query.filter_by(patientID=patientID).first()        
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
                patientAddress		=  patientAddress ,
                patientCity			=  patientCity	 ,
                patientState		=  patientState ,
                patientCountry		=  patientCountry ,
                patientpersonalEnroledby		=   patientpersonalEnroledby)
            db.session.add(new_patient)
            db.session.commit()
        except IntegrityError as e:
            return PatientEnrol(error=f'{e.orig}')
        return PatientEnrol(success = True, message=f'{patientLastname} {patientFirstname} with ID : {patientID}')
                        
        

        

   

class Mutation(graphene.ObjectType):
    save_post = CreatePost.Field()


# noinspection PyTypeChecker
schema_mutation = graphene.Schema(query=Query, mutation=Mutation)
