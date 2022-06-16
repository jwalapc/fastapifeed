from fastapi import APIRouter,Response,status,Request
from pydantic import BaseModel
from apimain.Lib.Signup_class import *
from apimain.Lib.Auth_class import *
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import starlette.status as status
from fastapi.websockets import WebSocket




router = APIRouter()

templates = Jinja2Templates(directory="templates")



class signup(BaseModel):
    name:str
    email:str
    password:str

@router.post('/auth/signup')
def signup(data:signup,response:Response):
    a=Signup()
    x=a.createuser(data.name.lower(),data.email.lower(),data.password.lower())
    if x:
        data={
            'Message': 'Signup Success',
            'Username': data.name,
            'Email': data.email,

        }
        response.status_code=200
        return data
    
    else:
        data = {
            'Error':'Signup Failure',
            'Message':'Email already exists',
        }
        response.status_code=409

        return data

class Login(BaseModel):
    email:str
    password:str

@router.get("/chat/{username}")
def chat(username:str,request: Request):
    a=checklogin(username)
    if a:
        return templates.TemplateResponse("feed.html",{"request":request,"username":username})
    else:
        return {"message":"Login to see feed"}


@router.post('/auth/login')
def login(data:Login,response:Response,request: Request):
    try:
        a=Auth(data.email.lower(),data.password.lower())
        data={
                'Message':'login Success',
                'Data':a.getdata(),
        }
        response.status_code=200
        s=a.getdata()
        username=s["Username"]
        return RedirectResponse(url=router.url_path_for('chat',username=username),status_code=status.HTTP_302_FOUND)
        return data
    except Exception as e:
        data={
                'Error':str(e),
            }
        response.status_code=401
        return data
    
class Isvalid(BaseModel):
    token:str
    
@router.post('/auth/isvalid')
def isvalid(data:Isvalid,response:Response):
    a=Auth(data.token)
    if a.authenticate():
        data={
            'Valid': True,
            'Valid_for':a.valid_for_token()
        }
        response.status_code=200
        return data
    else:
        data={
            'Error':'Invalid Token'
        }
        response.status_code=400
        return data

@router.post('/auth/logout/{username}')
def Logout(username:str,response:Response):
    a=userLogout(username)
    if a:
        data={
            'message': 'Logout successful'
        }
        response.status_code=200
        return data
    else:
        data={
            'message': 'Logout unsucessful'
        }
        response.status_code=400
        return data




