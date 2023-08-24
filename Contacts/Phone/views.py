from django.contrib.auth import authenticate, login as log_in, logout as log_out, login
from django.shortcuts import render
from Phone.models import *
from django.http import  HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    phone=Contacts.objects.all()
    return  render(request,'phone/index.html',{
        "phone":phone
    })

@login_required(login_url='login')
def details(request,id):
    detail=Contacts.objects.get(pk=id)
    phone = Contacts.objects.all()
    if request.method=="POST":
        contact=Contacts.objects.get(pk=id)
        Contacts.delete(contact)
        return render(request,'phone/index.html',{
            "detail":contact,
            "phone":phone
        })

    return render(request,'phone/details.html',{
        "detail":detail
    })


@login_required(login_url='login')
def show_add(request):
    if request.method=="POST":
        name=request.POST["name"]
        phone_number=request.POST["phone_number"]
        email_id=request.POST['email_id']
        address=request.POST["address"]
        contact=Contacts(name=name,phone_number=phone_number,email_id=email_id,address=address)

        contact.save()
        return HttpResponseRedirect(reverse('index'))

    return render(request,"phone/add.html")


@login_required(login_url='login')
def edit(request,id):
    if request.method=="POST":
        contact = Contacts.objects.get(pk=id)
        name=request.POST["name"]
        email_id=request.POST["email_id"]
        phone_number=request.POST["phone_number"]
        address=request.POST["address"]
        print(contact)
        contact.name=name
        contact.email_id=email_id
        contact.phone_number=phone_number
        contact.address=address
        contact.save()
        return HttpResponseRedirect(reverse('index'))
    contact=Contacts.objects.get(pk=id)
    return render(request,"phone/edit.html",{
        "contact":contact
    })


def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            log_in(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'phone/login.html',{
                "message":"invalid Credentials"
            })
    return render(request,'phone/login.html')

def logout(request):
    log_out(request)
    return  render(request,"phone/login.html",{
        "message":"you are Logged Out !!!"
    })
def delete(request):
    return render(request,"phone/details.html")

