from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse,HttpRequest
# Import the Smartphone model
from .models import Smartphone
import json
# Create your views here.
def add_product(reqeust: HttpRequest) -> JsonResponse:
    """add new product to database"""
    if reqeust.method == 'POST':
        # get body from request
        body = reqeust.body
        # get body data
        decoded = body.decode()
        # data to dict
        data = json.loads(decoded)
        # get all properties
        price = data.get('price', False)
        img_url = data.get('img_url', False)
        color = data.get('color', False)
        ram = data.get('ram', False)
        memory = data.get('memory', False)
        name = data.get('name', False)
        model = data.get('model', False)
        # Create a new smartphone object
          # check all properties is valid
        if price == False:
            return JsonResponse({"status": "price field is required."})
        if img_url == False:
            return JsonResponse({"status": "img_url field is required."})
        if color == False:
            return JsonResponse({"status": "color field is required."})
        if ram == False:
            return JsonResponse({"status": "ram field is required."})
        if memory == False:
            return JsonResponse({"status": "memory field is required."})
        if name == False:
            return JsonResponse({"status": "name field is required."})
        if model == False:
            return JsonResponse({"status": "model field is required."})

        # create a inctance of SmartPhone 
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

def cost(reqeust:HttpRequest):
    if reqeust.method == "GET":
        try:
            # get product from database by 
                data = reqeust.GET
                p = data['p']
                product = Smartphone.objects.filter(price__lte = p)

                json_data = []
                for i in product.all():
                    json_data.append({
                        "price": i.price,
                        "img_url": i.img_url,
                        "color": i.color,
                        "ram": i.ram,
                        "memory": i.memory,
                        "name": i.name,
                        "model": i.model
                    })
                return JsonResponse({"result":json_data})
        except ObjectDoesNotExist:
            return JsonResponse({"status": "object doesn't exist"})