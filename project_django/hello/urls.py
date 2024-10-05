from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('frank', views.frank, name='frank'),
]
