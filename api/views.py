from django.shortcuts import render
from django.http import JsonResponse,HttpRequest
# Create your views here.
def add_phone(request:HttpRequest):
    return JsonResponse({})