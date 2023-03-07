from django.shortcuts import render
from django.http import JsonResponse,HttpRequest
# Import the Smartphone model
from .models import Smartphone
import json
# Create your views here.
def add_phone(request:HttpRequest):
    if request.method=='POST':
        r = request.body
        data = r.decode()
        # Convert the data to a dictionary
        data = json.loads(data)
        price = data.get('price')
        img_url = data.get('img_url')
        color = data.get('color')
        ram = data.get('ram')
        memory = data.get('memory')
        name = data.get('name')
        model = data.get('model')

        # Create a new smartphone object
        phone = Smartphone()
        phone.price = price
        phone.img_url=img_url
        phone.color=color
        phone.ram=ram
        phone.memory=memory
        phone.name=name
        phone.model=model
        phone.save()
        
        

        return JsonResponse({'result':data})
    return JsonResponse({})