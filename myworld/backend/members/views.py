from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .main import *
from .pdf import *

def members(request):   
    print("hello")
    return HttpResponse("eunha")

def downloadyoutube(request):
    print("hello")
    link = request.GET["link"]
    class_notes, keywords, title, sum_array = yt2var(link)
    print(class_notes)
    print('keywords', keywords)
    print(title)
    toPdf(sum_array, keywords)
    data = JsonResponse({'title': title, 
        'class_notes': class_notes, 
        'keywords': keywords})
    return data

def downloadpdf(request):
    print('pdf!!!!')

