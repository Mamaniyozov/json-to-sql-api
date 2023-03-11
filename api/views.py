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

def get_all_product(request:HttpRequest):
    if request.method=='GET':
        # Get all the smartphone objects
        phones = Smartphone.objects.all()
        reslut = {
            'result':{
                
            }
        }
        # Loop through the objects and append them to the result dictionary
        for phone in phones:
            model = phone.model
            reslut.setdefault(model,[])
            reslut[model].append({          
                'id':phone.id,
                'price':phone.price,
                'img_url':phone.img_url,
                'color':phone.color,
                'ram':phone.ram,
                'memory':phone.memory,
                'name':phone.name,
                'created_at':phone.created_at,
                'updated_at':phone.updated_at,
                
            })

    return JsonResponse(reslut)
    
def get_product_by_model(request:HttpRequest,model):
    if request.method=='GET':
        # Get all the smartphone objects
        phones = Smartphone.objects.filter(model__contains=model)
        reslut = {
            'model':model,
            'result':[]
        }
        # Loop through the objects and append them to the result dictionary
        for phone in phones:
            reslut['result'].append({          
                'id':phone.id,
                'price':phone.price,
                'img_url':phone.img_url,
                'color':phone.color,
                'ram':phone.ram,
                'memory':phone.memory,
                'name':phone.name,
                'created_at':phone.created_at,
                'updated_at':phone.updated_at,
                
            })
    return JsonResponse(reslut)
                             

# Update a product
def update_price(request:HttpRequest,pk):
    if request.method=='GET':
        # Get the smartphone object
        phone = Smartphone.objects.get(id=pk)
        # Get the price from the request
        price = phone.price+10
        # Update the price
        phone.price = price
        phone.save()
        

    return JsonResponse({
        'name':phone.name,
        'price':phone.price,
        'model':phone.model,
        'color':phone.color,
        'ram':phone.ram,
    })

