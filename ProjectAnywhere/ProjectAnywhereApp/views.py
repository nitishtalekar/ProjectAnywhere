from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    d = {'val':[1]*5, 'x':'Login | '}
    return render(request, 'PAA/index.html', d)

def home(request):
    d = {'x':'Home | '}
    return render(request, 'PAA/home.html', d)
