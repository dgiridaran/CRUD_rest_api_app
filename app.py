from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,ItemList
from db import db
from resources.store import Store,StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_data.db'
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