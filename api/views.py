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
        price = data['price'] 
        img_url = data['img_url']
        color = data['color']
        ram = data['ram']
        memory = data['memory']
        name = data['name']
        model = data['model']
        # Create a new smartphone object
        phone = Smartphone()
        phone.price = price
        phone.save()
        
        

        return JsonResponse({'result':data})
    return JsonResponse({})