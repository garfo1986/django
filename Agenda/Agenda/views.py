
import email
from django.shortcuts import render, redirect
from agendaapp.models import Contacts



# Create your views here.
def Contact(request):
    contact=Contacts.objects.all()

    return render (request, 'index.html',{"contacts":contact})


def other(request):
    contact=Contacts.objects.all()
    return render (request, 'other.html',{"contacts":contact})

def edit(request):
    contact=Contacts.objects.all()
    return render (request, 'edit.html',{"contacts":contact})

def addcontact(request):
    contact=Contacts.objects.all()
    return render (request, 'addcontact.html')

def registercontact(request):
    name=request.POST['txtName']
    phone=request.POST['txtPhone']
    Email=request.POST['txtEmail']

    contact=Contacts.objects.create(name=name, phone_number= phone, email =Email)

    return redirect('/agenda/') #la ruta redirect debe ser importada

def deletedata(request, id):
    data = Contacts.objects.get(id=id)
    data.delete()
    
    return redirect('/agenda/')

def selectdata(request, id):
    contact = Contacts.objects.get(id=id)
    return render(request, 'editdata.html',{"contact":contact})

def updatedata(request):
    id=request.POST['txtid']
    name=request.POST['txtName']
    phone=request.POST['txtPhone']
    Email=request.POST['txtEmail']

    contact = Contacts.objects.get(id=id)
    contact.name = name
    contact.phone_number = phone
    contact.email=Email

    contact.save()

    return redirect('/agenda/')
