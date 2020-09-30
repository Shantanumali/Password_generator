from django.shortcuts import render
import string
import random
from django.http import HttpResponse

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    lt = int(request.GET.get('length', 8))
    s = ""
    while(True):
        if lt > 1:
            s += random.choice(list(string.ascii_lowercase))
            lt -= 1
            if lt <1:
                break
        else:
            break
        if request.GET.get('Uppercase'):
            s += random.choice(list(string.ascii_uppercase))
            lt -= 1
            if lt <1:
                break
        if request.GET.get('Numbers'):
            s += random.choice(list(string.digits))
            lt -= 1
            if lt < 1:
                break
        if request.GET.get('Special'):
            s += random.choice(list(string.punctuation))
            lt -= 1
            if lt < 1:
                break
    thepassword = s
    return render(request, 'generator/password.html', {'password': thepassword})