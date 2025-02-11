from django.shortcuts import render,HttpResponse
import random
import string  
# Create your views here.

def random_password(request):
    characters = string.ascii_letters + string.digits + string.punctuation  
    password = ''.join(random.choice(characters) for i in range(9))   
    return HttpResponse({password})