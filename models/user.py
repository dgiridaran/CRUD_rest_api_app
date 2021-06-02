from db import db

class UserModel(db.Model):  #This db.Model is says the sqlalchamy that this class is used for send and recive the data in the data base.
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True) #primary_key means each index are unique,No repeting index values.
    username = db.Column(db.String(80)) #The string(80) means the username has a limit of 80 charactors.
    password = db.Column(db.String(80)) #The string(80) means the password has a limit of 80 charactors.

    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first() #query methord will create the query automatically with salalchamy.

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first()