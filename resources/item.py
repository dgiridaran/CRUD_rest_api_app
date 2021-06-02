from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()  #This will provide some contrains for the  parametors like we can only change price in this.
    parser.add_argument('price',
    type=float,
    required = True,
    help = 'This field cannot be left blank!'
    )

    parser.add_argument('store_id',
    type=int,
    required = True,
    help = 'Every item need a store_id.'
    )

    @jwt_required()  #Because of this decoretor(),we have to authenticate before this get methord. This decoretor is used to call identity function in security,To identify the user by JWT.
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return{"message":"Item not found"},404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':"An item with this name '{}' is exist.".format(name)},400
        data = Item.parser.parse_args()
        item = ItemModel(name,data['price'],data['store_id'])
        try:
            item.save_to_db()
        except:
            {"message":"An Error occured inserting the item"},500
        return item.json(),201

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            
        return {'message':'Item deleted'}

    def put(self,name):
        data = Item.parser.parse_args() #This will only allow the price argument any other argument sent as an input will be eraised.
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name,data['price'],data['store_id'])   
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items': [x.json() for x in ItemModel.query.all()]}
        