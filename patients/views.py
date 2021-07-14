import datetime
import hashlib
import uuid

import django
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PatientForm, UserForm
from .models import Patient, Session, User

# Get response with list of all patients.
def plist(request):
    if checkCookies(request):
        """
        return render(request, 'patients/list.html')
        """

        patients = Patient.objects.all
        return render(request, 'patients/list.html', {'tittle': 'Список','patients':patients})
    else:
        return redirect('/login')

def checkCookies(request):
    if 'auth_token' in request.COOKIES:
        t = Session.objects.filter(auth_token=request.COOKIES['auth_token']).last()
        if datetime.datetime.now().hour - t.last_used.hour > 144:
            t.delete()
            return False
        else:
            t.last_used = datetime.datetime.now()
            return True

# Get response with patient add menu.
def add(request):
    if checkCookies(request):
        form = PatientForm()
        if request.method == 'POST':
            print(request.POST)
            form = PatientForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'patients/add.html', context)
    else:
        return redirect('/login')


def login(request):
    if request.method == 'POST':
        if User.objects.filter(login=request.POST['login']).exists():
            user = User.objects.filter(login=request.POST['login']).first()
        else:
            return HttpResponse('Net')

        if hashlib.sha256(str(request.POST['password']).encode('UTF-8')).hexdigest() == user.password_hash:
            if Session.objects.filter(login=user).exists():
                response = HttpResponseRedirect('/')
                response.set_cookie('auth_token', Session.objects.filter(login=user).first().auth_token)
                return response
            else:
                t = uuid.uuid4()
                Session.objects.create(login=user.login, last_used=datetime.datetime.now(), auth_token=t)
                response = HttpResponseRedirect('/')
                response.set_cookie('auth_token', t)
                return response

    return render(request, 'patients/login.html')


# Get response with patient add menu.
def addUser(request):
    if checkCookies(request):
        form = UserForm()
        if request.method == 'POST':
            print(request.POST)
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'patients/adduser.html', context)
    else:
        return redirect('/login')


def qrTest(request, uuid):
    args = {'uuid': uuid}
    return render(request, 'patients/qr.html', args)
