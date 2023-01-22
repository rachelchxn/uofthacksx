from django.shortcuts import render
from django.http import HttpResponse
# from .script import CoolClass
from .main import *
# from .models import Notes

# class NotesView(viewsets.ModelViewSet):  
#     serializer_class = TodoSerializer   
#     queryset = Todo.objects.all()    

def members(request):   
    return HttpResponse("eunha")

def downloadyoutube(request):
    link = request.GET["link"]
    class_notes, keywords, title = yt2var(link)
    print(class_notes)
    print('keywords', keywords)
    print(title)
    data = [title, class_notes, keywords]
    return data

