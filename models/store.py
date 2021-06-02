from db import db

class StoreModel(db.Model): #This db.Model is says the sqlalchamy that this class is used for send and recive the data in the data base.
    __tablename__ = 'stores'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80)) #The string(80) means the name has a limit of 80 charactors.
    items = db.relationship('ItemModel',lazy='dynamic') #This will connect the items to the store using store_id.


    def __init__(self,name):
        self.name = name

    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() #this will automatically creates the query and return the item object using sqlalchemy.

    def save_to_db(self):
        db.session.add(self) #using session  key word we can add multile objects to the database.
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    