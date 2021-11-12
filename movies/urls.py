from django.urls import path
from . import views

app_name='movies'
urlpatterns=[
    path('', views.index, name='index'),
    path('recommend/', views.recommend, name='recommend'),
    path('weather/', views.weather, name='weather'),

]