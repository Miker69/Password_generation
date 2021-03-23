from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        chars = ''.join(chars)
        chars = chars + chars.upper()
        chars = list(chars)
    if request.GET.get('special_characters'):
        chars.extend(list('!@#$%^&*()?_|'))

    if request.GET.get('numbers'):
            chars.extend(list('0123456789'))


    leng = int(request.GET.get('length', 20))
    thepassword = ''
    for x in range(leng):
        thepassword += random.choice(chars)
    return render(request, 'generator/password.html', {'password': thepassword})
