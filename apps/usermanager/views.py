from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .services import usercreate,userdetails,userupdate,userdelete,userlist

@api_view(['GET', 'POST'])
def usercreateanduserlist(request):
    usertype=request.usertype
    if usertype is not None:
        if request.method == 'GET':
            if usertype=="customer":
                res=userlist.userlist()
                return Response(res)
            else:
                return Response('you are not authorized')

        elif request.method == 'POST':
            username=request.data['username']
            email=request.data['email']
            password=request.data['password']
            

            if usertype=='manager':
                res=usercreate.createuser(username,email,password)
                
                return Response({
                    "success":True,
                    "token":res
                    }
                )
            else:
                return Response(
                    {
                        "success":False,
                        "Message":"You are not authoritzed to create a user"
                    }
                )
    else:
        return Response("you are not authorized")

@api_view(['GET', 'PUT','DELETE'])

def usermanage(request,username):
        
        usertype=request.usertype
        if usertype is not None:
            if request.method=="GET":
            
                if usertype=='customer':
                    res=userdetails.userdetails(username)
                    return Response(res)
                else:
                    return Response("you are not authorized")
                
            elif request.method=="PUT":
            
                data=request.data
            
                if usertype=='manager':
                    res=userupdate.userupdate(username,data)
                    return Response(res)
                    
                else:
                    return Response("you are not authorized")
                    
            elif request.method=="DELETE":
                if usertype=='manager':
                    res=userdelete.userdelete(username)
                    return Response(res)
                    
                else:
                    return Response("you are not authorized")
        else:
            return Response("you are not authorized")
            
    

        