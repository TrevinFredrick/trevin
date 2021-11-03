from django.shortcuts import render
from django.http import HttpResponse, response
from rest_framework.decorators import api_view
from rest_framework.response import Response
import trevinapp
# Create your views here.
def fnsample(request):
    return HttpResponse("Trevin")
@api_view(['GET'])
def fntrevin_api(request):
    return Response("you have created an api")
@api_view(['GET','POST'])
def helloworld(request):
    if request.method =='POST':
    
        return Response({"message":"i got some data","data":request.data})
    return Response({"message":"i am trevin"})
@api_view(['POST'])
def saveusername(request):
    newname=request.data['username']
    print(newname)
    file1=open('trevin/users.txt','a+')
    status='user not saved'
    with open('trevin/users.txt') as myfile:
        if newname in myfile.read():
            status="user already exist"
        else:
            file1.write('\n'+ newname)
            status="user saved succesfully"
    file1.close()
    return Response(status)
@api_view(['POST'])
def savepassword(request):
    newpassword=request.data['password']
    print(newpassword)
    status='invalid password'
    l,u,p,d=0,0,0,0
    if (len(newpassword)>=8):
        for i in newpassword:
            if i.islower():
                l+=1
            if i.isupper():
                u+=1
            if i.isdigit():
                d+=1
            if (i=='@'or i=='$'or i=='#' or i=='*'):
                p+=1
            # print(l,u,p,d)
            if l>=1 and u>=1 and p>=1 and d>=1 and l+u+p+d==len(newpassword):
                status='valid password'
                # print(status)
            else:
                # print('invalid')
                status='invalid'
        
    return Response(status)
@api_view(['GET'])
def checkusername(request):
    username=request.data['username']
    file1=open('trevin/users.txt','r+')
    user=file1.read().splitlines()
    file1.close()
    status='username not found'
    if username in user:
        status='valid username'
    return Response(status)
            
            
         







     



