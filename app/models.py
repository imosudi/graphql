# ------------------  Database Models ------------------
from unicodedata import name
from .import db
from .models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, \
                       String, ForeignKey
                       

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    email = db.Column(db.String(256), index=True, unique=True)  # index => should not be duplicate
    posts = db.relationship('Post', backref='author')

    def __repr__(self):
        return '<User %r>' % self.email


class Post(db.Model):
    __tablename__ = 'posts'
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(256))
    body        = db.Column(db.Text)
    author_id   = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % self.title


# Define models
roles_users = db.Table('roles_users',
                        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model) :      #, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repre__(self):
        return '<Role %r>' % self.name
        


class User(db.Model) :              # UserMixin, db.Model):
    __tablename__ = 'user'
    id                  = db.Column(db.Integer, primary_key=True)
    email 		        = db.Column(db.String(100), unique=True)
    password 		    = db.Column(db.String(255))
    #username 		    = db.Column(db.String(100), unique=True)
    last_login_at 	    = db.Column(db.DateTime())
    current_login_at 	= db.Column(db.DateTime())
    last_login_ip 	    = db.Column(db.String(100))
    current_login_ip 	= db.Column(db.String(100))
    login_count 	    = db.Column(db.Integer)
    active 		        = db.Column(db.Boolean()) 
    confirmed_at 	    = db.Column(db.DateTime())
    firstname 		    = db.Column(db.String(255))
    lastname 		    = db.Column(db.String(255)) 
    phonenumber 	    = db.Column(db.String(100), unique=True)
    altnumber		    = db.Column(db.String(100))
    designation	        = db.Column(db.String(100))
    location		    = db.Column(db.String(100))
    city		        = db.Column(db.String(100))
    state 		        = db.Column(db.String(100))
    country 		    = db.Column(db.String(100))
    zip_code		    = db.Column(db.String(100))
    roles 		        = db.relationship('Role', secondary=roles_users, 
                            backref=db.backref('users', lazy='dynamic')) 
    def __repr__(self):
        return '<User %r>' % self.email

            

class Transactions(db.Model):
    __tablename__ = 'transactions'
    transaction_id 		= db.Column(db.Integer, primary_key=True)
    CurrentpatientID 	= db.Column(db.String(100))
    barcode 			= db.Column(db.String(100), unique=True)
    
    fullName	 		= db.Column(db.String(100))
    regtype	 		    = db.Column(db.String(100))
    sex	 		        = db.Column(db.String(100))
    billto	 		    = db.Column(db.String(100))
    testspriority	 	= db.Column(db.String(100))
    testscheduletype	= db.Column(db.String(100))
    
    subtotal			= db.Column(db.String(100))
    discount			= db.Column(db.String(100))
    equalltax			= db.Column(db.String(100))
    total	 		    = db.Column(db.String(100))
    
    paymentmethod 		= db.Column(db.String(100))
    payment		 	    = db.Column(db.String(100))
    referenceOrchange	= db.Column(db.String(200))
    sessionconfirm		= db.Column(db.String(100))
    paymentconfirm		= db.Column(db.String(100))
    cashier			    = db.Column(db.String(100))
    #barcode			= db.Column(db.String(100)) # Column Duplication
    
    invoicemnemonics		= db.Column(db.String(2100))
    invoicetestname		    = db.Column(db.String(2100))
    invoiceprice		    = db.Column(db.String(2100))
    invoicetat			    = db.Column(db.String(2900))
    
    transactTime		    = db.Column(db.DateTime, server_default=db.func.now())
    phlebotomy_processed	= db.Column(db.Boolean(), default=False) 
    paymentupdateamount	    = db.Column(db.String(100))
    paymentupdateby		    = db.Column(db.String(100))
    paymentupdateTime		= db.Column(db.DateTime, server_default=None) # nullable=False),

    def __repr__(self):
        return '<Transactions %r>' % self.barcode
        '''self.TransactionId
        self.CurrentpatientID
        self.barcode
        self.billto
        self.fullName
        self.subtotal
        self.total
        self.payment
        self.paymentmethod
        self.transactTime
        self.cashier'''
    
class Patients(db.Model):
    __tablename__ = 'patients'
    patient_id 			    = db.Column(db.Integer, primary_key=True)
    
    patientFirstname		= db.Column(db.String(100))
    patientLastname			= db.Column(db.String(100))
    patientMiddlename		= db.Column(db.String(100))
    patientSex				= db.Column(db.String(100))
    patientTitle			= db.Column(db.String(100))
    ageGrade				= db.Column(db.String(100))
    patientDateofBirth		= db.Column(db.String(100))
    #patientAge			    = db.Column(db.String(100))
    patientStatus			= db.Column(db.String(100))
    patientType			    = db.Column(db.String(100))
    patientID				= db.Column(db.String(100), unique=True)	
    # patientLastname[:3] + "-" + patientFirstname[:2] + "-" + {{ moment(current_time).format('YYYYMM') + patientSex[0]}}
    patientEmail			= db.Column(db.String(100))#, unique=True)
    patientAltEmail			= db.Column(db.String(100))
    patientPhonenumber		= db.Column(db.String(100)) #, unique=True)
    patientAltPhonenumber	= db.Column(db.String(100))
    patientwhatsappnumber	= db.Column(db.String(100))
    
    patientAddress			= db.Column(db.String(100))
    #patientAddress2		= db.Column(db.String(100))
    patientCity			    = db.Column(db.String(100))
    patientState			= db.Column(db.String(100))
    patientCountry			= db.Column(db.String(100))
    #patientZip			    = db.Column(db.String(100))
    patientpersonalEnroledby		= db.Column(db.String(100))
    
    patientCompanyname			    = db.Column(db.String(100))
    patientCorporateContactperson	= db.Column(db.String(100))
    patientCorporateEmail		    = db.Column(db.String(100))
    patientAltCorporateEmail		= db.Column(db.String(100))
    patientCorporatePhone		    = db.Column(db.String(100))
    patientCorporateAltPhone		= db.Column(db.String(100))
    patientCorporatewhatsappnumber	= db.Column(db.String(100))
    patientCorporateAddress		    = db.Column(db.String(100))
    #patientCorporateAddress2		= db.Column(db.String(100))
    patientCorporateCity		    = db.Column(db.String(100))
    patientCorporateState		    = db.Column(db.String(100))
    patientCorporateCountry		    = db.Column(db.String(100))
    #patientCorporateZip		    = db.Column(db.String(100))
    patientCorporateEnroledby		= db.Column(db.String(100))
    enrolment_Time			        = db.Column(db.DateTime, server_default=db.func.now())
    
    def __repr__(self):
        #return '<Patients %r >' % self.patientID
        return '<Patients %r %r %r %r %r %r >' % self.id, self.patientID, self.patientLastname,
        self.patientSex, self.ageGrade, self.patientFirstname
    '''def __repr__(self):
        return '<Patients {} {} {} {} {} {}>'.format(self.id, self.patientID, self.patientLastname,
        self.patientSex, self.ageGrade, self.patientFirstname)'''
        
class Labtests(db.Model):
    __tablename__ = 'labtests'
    test_id 			= db.Column(db.Integer, primary_key=True)
    testType	 		= db.Column(db.String(100)) # CLINICAL_CHEMISTRY, ENDOSEROLOGY, HAEMATOLOGY, MICROBIOLOGY, SEROLOGY
    testBottleType		= db.Column(db.String(100))
    testName	 		= db.Column(db.String(200))
    testmnemonics 		= db.Column(db.String(100))
    testDetails	 	    = db.Column(db.String(2000))
    testTAT			    = db.Column(db.String(100))
    testPrice			= db.Column(db.String(100)) 

    '''def __repr__(self):
        return '<Labtests %r %r %r %r>' % self.test_id, self.testName, self.testmnemonics, self.testType)
'''
    def __repr__(self) :
        return '<Labtests {} {} {} {}>'.format(self.test_id, self.testName, self.testmnemonics, self.testType)
