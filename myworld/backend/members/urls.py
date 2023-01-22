from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('downloadyoutube/',views.downloadyoutube,name='downloadyoutube'),
    path('downloadpdf/',views.downloadpdf,name='downloadpdf'),
]