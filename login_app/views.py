from django.shortcuts import render,redirect,HttpResponse
from .models import *
import bcrypt
from django.contrib import messages
from datetime import datetime
from login_app.models import *


def login_page(request):
    context = {
        "login_page" : True,
    }
    return render(request,"login_page.html",context)

def success(request):
    user_id = request.session.get('user_id')
    if user_id:
        context = {
            'user' : User.objects.get(id=user_id)
        }
        return render(request,"success.html",context)
    else:
        return redirect('/')

def register(request):
    # request.session.flush()
    errors = User.objects.registerValidator(request.POST)
    request.session['errors'] = errors
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    birthday = request.POST['birthday']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    request.session['first_name'] = first_name
    request.session['last_name'] = last_name
    request.session['birthday'] = birthday
    request.session['email'] = email
    request.session['password'] = password
    request.session['confirm_password'] = confirm_password
    if len(errors) > 0:
        # for key, value in errors.items():
        #     messages.error(request,value)
        return redirect('/login')
    else:
        request.session.flush()
        # confirm_password = request.POST['confirm_password']
        password_bcrypt = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        user = User.objects.create(first_name=first_name,last_name=last_name,birthday=birthday,email=email,password=password_bcrypt)
        request.session['user_id'] = user.id
        # if 'errors' in request.session.keys():
        #     del request.session['errors']
        return redirect('/user_experience')

def login(request):
    request.session.flush()
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        request.session['errors'] = errors
        request.session['login_email'] = request.POST['login_email']
        request.session['login_password'] = request.POST['login_password']
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/login')
    else:
        # request.session.flush()
        email = request.POST['login_email']
        # password = request.POST['login_password']
        user = User.objects.filter(email=email)[0]
        request.session['user_id'] = user.id
        # if 'errors' in request.session.keys():
        #     del request.session['errors']
        return redirect('/user_experience')
    


def logout(request):
    request.session.flush()
    return redirect('/login')

def child(request):
    context = {
    }
    return render(request,"child.html",context)
