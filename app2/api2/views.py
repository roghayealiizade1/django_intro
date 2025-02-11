from django.shortcuts import render,HttpResponse
import random
import string  
import requests
from django.http import JsonResponse 
# Create your views here.e 

def random_password(request):
    characters = string.ascii_letters + string.digits +string.punctuation
    password = ''.join(random.choice(characters) for i in range(9))   
    return HttpResponse({password})

def random_number():
    random_number = random.randint(1, 1000)
    url = "NUMBER/com.numbersapi://http"
    response = requests.post(url, json={"number": random_number})
    if response.status_code == 200:
        print("متن:", response.text)
    else:
        print( "خطا", response.status_code)
        random_number()
 
import requests

def weather_info():
    url = "https://wttr.in/Kerman?format=j1"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        current_condition = weather_data['current_condition'][0]
        temp_c = current_condition['temp_C']
        windspeed_kmph = current_condition['windspeedKmph']
        humidity = current_condition['humidity']
        weather_info = f"دمای فعلی: {temp_c} درجه سانتی‌گراد، سرعت باد: {windspeed_kmph} کیلومتر بر ساعت، رطوبت: {humidity} درصد"
        print(weather_info)
    else:
        print("خطا:", response.status_code)
    weather_info()