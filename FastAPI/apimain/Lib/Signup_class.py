import pymongo
import json
import passlib.context as p
from apimain.Lib.client import *


# client=pymongo.MongoClient('localhost')
db=client.Intern
Users=db.Users
Home=db.Home

pwd_context = p.CryptContext(schemes=["bcrypt"], deprecated="auto")



def get_password_hash(password):
    return pwd_context.hash(password)

class Signup:

    def __init__(self):
        pass

    def createuser(self, username,email, password):
        data = {
            'username':username.lower(),
            'email': email,
            'Password': password,
        }
        a = Users.find()
        for i in a:
            # print(i)
            if i['email'] == email:
                print('Email already exists')
                return False
        else:
            data['Password']=get_password_hash(data['Password'])
            Users.insert_one(data)

            return True

    def verifytoken(self,username,password):
        pass








