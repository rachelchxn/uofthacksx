from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# from .script import CoolClass
from .main import *
# from .models import Notes

# class NotesView(viewsets.ModelViewSet):  
#     serializer_class = TodoSerializer   
#     queryset = Todo.objects.all()    

def members(request):   
    print("hello")
    return HttpResponse("eunha")

def downloadyoutube(request):
    print("hello")
    link = request.GET["link"]
    class_notes, keywords, title = yt2var(link)
    print(class_notes)
    print('keywords', keywords)
    print(title)
    data = JsonResponse({'title': title, 
             'class_notes': class_notes, 
              'keywords': keywords})
    return data

