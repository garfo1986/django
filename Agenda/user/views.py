from collections import UserList

from django.shortcuts import HttpResponse
from django.shortcuts import render
from user.models import user_database
from django.shortcuts import render, redirect
from hashlib import sha1

# Create your views here.


def userlist(request):
    user=user_database.objects.all
    return render (request, 'userstemplates/userlist.html',{"users":user})

def adduser(request):
    return render (request, 'userstemplates/adduser.html')

def addusersend(request):
    name=request.POST['txtName']
    last_name=request.POST['txtLastName']
    Email=request.POST['txtEmail']
    password=request.POST['txtPassword']

    encrypted = (sha1(password.encode("utf-8")).hexdigest())

    user=user_database.objects.create(name=name, last_name=last_name, email =Email, password=encrypted)

    return redirect('/userlist/') #la ruta redirect debe ser importada

def identify(request):
    
    return render (request, 'userstemplates/identifyuser.html')
    

def checkuserlogin(request):
    
    if request.GET["txtEmail"]:
       #mensaje= "Articulo buscado: %r" %request.GET["txtEmail"]
       query=request.GET["txtEmail"]
       query2=request.GET["txtPassword"]
       encrypted = (sha1(query2.encode("utf-8")).hexdigest())
       #encrypted2=type(encrypted2)
       #user=user_database.objects.filter(email__icontains=query)#the email__icontains is the name of the field in the database
       #el icontains is a search similar to "like" 
       user=user_database.objects.filter(email=query, password=encrypted)
       return render(request, "userstemplates/access.html", {"user": user, "query": query,"query2":query2})

    else:
        mensaje= "please include your info"
        
    #return HttpResponse(mensaje) #httpResponse must be import