from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ProjectAnywhereApp.forms import *
from .models import *


# Create your views here.
def index(request):
    d = {'val':[1]*5, 'x':'Login | '}
    return render(request, 'PAA/index.html', d)

def login(request):
    form = LoginForm()
    d = {'x':'Home | ',
    'form':form}
    data = []
    if request.method == "POST":
        if form.is_valid():
            # if 'login' in request.POST:
            data.append(form.cleaned_data['user_name'])
            data.append(form.cleaned_data['password'])
            d = {'form':form,'data':data}
            return render(request, 'PAA/login.html',d)

    return render(request, 'PAA/login.html', d)


def signup(request):
    udata = []
    if request.method == "POST":
        signup = SignupForm(request.POST)
        data = []

        if signup.is_valid():
            udata.append(signup.cleaned_data['email'])
            udata.append(signup.cleaned_data['user_name'])
            pwd = signup.cleaned_data['password']
            rpwd = signup.cleaned_data['reenter_password']
            if pwd == rpwd:
                udata.append(signup.cleaned_data['password'])
            else:
                return HttpResponseRedirect('/signup/')
            udata.append(signup.cleaned_data['first_name'])
            udata.append(signup.cleaned_data['last_name'])


            userdata = Users(email = udata[0], user_name = udata[1], password = udata[2], fname = udata[3], lname = udata[4])
            userdata.save()
            return render(request, 'PAA/user.html', {'udata':udata})

    else:
        signup = SignupForm()
        d = {'x':'Home | ','signup':signup}
        return render(request, 'PAA/signup.html', d)

def admin(request):
    d = {'x':'Home | '}
    return render(request, 'PAA/admin.html', d)

def user(request):
    d = {'x':'Home | '}
    return render(request, 'PAA/user.html', d)
