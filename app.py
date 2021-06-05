import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,ItemList
from db import db
from resources.store import Store,StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgresql://aznxgvsytfhige:686bd9aa22e414db10ef2b101ec2b84fe782bfa46d147933745e46b981edc1cc@ec2-34-232-191-133.compute-1.amazonaws.com:5432/d1v9748i01luna','sqlite:///my_data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #This to turn off the flask modification tracker.But still the sqlalchamy modification tracker workes,which is better.
app.secret_key = 'giri' #This is the signature in the JWT ,So it should be long and secret.
api = Api(app)

jwt = JWT(app,authenticate,identity) #/auth,we dont create this the jwt extenshion create this for us.It will recive a username and password from client,checks and returns a JWT tocken.

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') #The resource methord is used to connect the methord you created with the end point.
api.add_resource(ItemList, '/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000)