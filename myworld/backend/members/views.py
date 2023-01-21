from django.shortcuts import render
from django.http import HttpResponse
from .script import CoolClass

def members(request):   
    return HttpResponse("Hello world!")

def downloadyoutube(request):
    audio = CoolClass()
    #audio.test()
    link = request.GET["link"]
    return HttpResponse(200)