from django.urls import path
from . import views

urlpatterns = [
    path('', views.client,),
    path('resume', views.index, name="index"),
    
    
]

