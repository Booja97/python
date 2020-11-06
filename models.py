from db import db

class Customers(db.Document):
    name=db.StringField()
    username=db.StringField()
    password=db.StringField()
    address=db.StringField()
    state=db.StringField()
    country=db.StringField()
    email=db.StringField()
    pan=db.StringField()
    contact=db.StringField()
    dob=db.StringField()
    accounttype=db.StringField()

class Loan(db.Document):
    username=db.StringField()
    loantype=db.StringField()
    loanamount=db.StringField()
    date=db.StringField()
    rateofinterest=db.StringField()
    durationofloan=db.IntField()