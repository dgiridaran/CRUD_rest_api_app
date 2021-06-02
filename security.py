from models.user import UserModel
from werkzeug.security import safe_str_cmp #This methord is used to comare the two strings.

def authenticate(username,password): #here the JWT encriped code will be made.
    user=UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload): #the payload is the JWT created by the auth,user id is encoaded init.That is extracted using the payload['identity']...##here we take the information from the encripted code.
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)





