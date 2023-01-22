from django.shortcuts import render
from django.http import HttpResponse
from .script import CoolClass
from .main import *

def members(request):   
    return HttpResponse("eunha")

def downloadyoutube(request):
    link = request.GET["link"]
    class_notes, keywords = yt2var(link)
    print(class_notes)
    print('keywords', keywords)
    return HttpResponse('worked')

