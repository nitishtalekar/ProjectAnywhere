from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ProjectAnywhereApp.forms import *
from .models import *


# Create your views here.
def index(request):
    d = {'val':[1]*5, 'x':'Login | '}
    request.session['error'] = ""
    return render(request, 'PAA/index.html', d)

def login(request):
    e = request.session['error']
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['user_name']
            pwd = form.cleaned_data['password']
            log = Users.objects.filter(user_name = u, password=pwd)
            if log.count() == 1:
                d = {'uname':u}
                return render(request, 'PAA/user.html',d)
            else: 
                request.session['error'] = "Username or Password Incorrect"
                return HttpResponseRedirect('/login/')
    else:
        form = LoginForm()
        d = {'x':'Home | ','form':form, "errors":e}
        return render(request, 'PAA/login.html', d)


def signup(request):
    udata = []
    e = request.session['error']
    if request.method == "POST":
        data = []
        signup = SignupForm(request.POST)
        print("1")
        if signup.is_valid():
            print("2")
            udata.append(signup.cleaned_data['email'])
            udata.append(signup.cleaned_data['user_name'])
            email = Users.objects.filter(email = udata[0])
            user_name = Users.objects.filter(user_name = udata[1])
            if email.count() == 0 and user_name.count() == 0:
                pwd = signup.cleaned_data['password']
                rpwd = signup.cleaned_data['reenter_password']
                if pwd == rpwd:
                    udata.append(signup.cleaned_data['password'])
                else:
                    request.session['error'] = "Passwords Do Not Match"
                    return HttpResponseRedirect('/signup/')
                udata.append(signup.cleaned_data['first_name'])
                udata.append(signup.cleaned_data['last_name'])
                userdata = Users(email = udata[0], user_name = udata[1], password = udata[2], fname = udata[3], lname = udata[4])
                userdata.save()
                return render(request, 'PAA/user.html', {'uname':udata[1]})
            else:
                request.session['error'] = "Email or Username ALready Exists"
                return HttpResponseRedirect('/signup/')
        else:
            request.session['error'] = "Enter valid Email"
            return HttpResponseRedirect('/signup/')
            
    else:
        signup = SignupForm()
        d = {'x':'Home | ','signup':signup,"errors":e}
        return render(request, 'PAA/signup.html', d)

def admin(request):
    d = {'x':'Home | '}
    return render(request, 'PAA/admin.html', d)

def user(request):
    d = {'x':'Home | '}
    return render(request, 'PAA/user.html', d)
    
def add_project(request):
    add_project = AddProject()
    d = {'x':'Home | ','add_project':add_project}
    return render(request, 'PAA/add_project.html', d)
    
def status(request):
    d = {'x':'Home | '}
    return render(request, 'PAA/status.html', d)
