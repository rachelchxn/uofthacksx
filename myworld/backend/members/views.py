from django.shortcuts import render
from django.http import HttpResponse
from .script import CoolClass

def members(request):   
    return HttpResponse("eunha")

def downloadyoutube(request):
    audio = CoolClass()
    print('download request')
    #audio.test()
    try:
        link = request.GET["link"]
        print(link)
        audio.download_file(link)
        return HttpResponse('worked')
    except:
        print('failed')
        return HttpResponse('invalid url')