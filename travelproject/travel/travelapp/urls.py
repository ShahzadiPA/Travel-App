from . import views
from django.urls import path


urlpatterns = [

    path('', views.demo, name='demo'),
   # path('operators/', views.arithmeticOperations, name='arithmeticOperations'),
   # path('contact/', views.contact, name='contact')
]
