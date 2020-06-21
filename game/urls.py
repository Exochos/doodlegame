from django.urls import path
from . import views

#Urls we are starting with a basic index page
urlpatterns=[
	path('', views.index, name='index'),
]

