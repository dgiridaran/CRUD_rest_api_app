from db import db

class ItemModel(db.Model): #This db.Model is says the sqlalchamy that this class is used for send and recive the data in the data base.
    __tablename__ = 'items'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80)) #The string(80) means the name has a limit of 80 charactors.
    price = db.Column(db.Float(precision=2)) #precision is the numbers after the decimal point.
    store_id = db.Column(db.Integer,db.ForeignKey('stores.id')) #This will create a store_id int in each item,with will represents a store. 
    store = db.relationship('StoreModel') #This will connect the store with the store id in each item.

    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() #this will automatically creates the query and return the item object using sqlalchemy.

    def save_to_db(self):
        db.session.add(self) #using session  key word we can add multile objects to the database.
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    