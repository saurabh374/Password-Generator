from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, "generator/home.html")
    # return HttpResponse("Hello World")
def password(request):
    Characters = 'abcdefghijklmnopqrstuvwxyz'
    length = int(request.GET.get('length',12))
    thepassword = ''
    if request.GET.get('uppercase'):
        Characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if request.GET.get('special'):
        Characters += '!@#$%^&*()'
    if request.GET.get('numbers'):
        Characters += '0123456789'
    for x in range(length):
        thepassword += random.choice(Characters)
    return render(request, "generator/password.html", {'password':thepassword})

def about(request):
    return render(request, "generator/about.html")
