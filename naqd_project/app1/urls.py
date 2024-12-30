from django.urls import path     
from . import views
urlpatterns = [
    path('', views.login),   
    path('register', views.register), 
    path('main', views.main,name="main"),
    path('api/customers/', views.customers_list, name='customers-list'),
    path('api/debts/', views.debts_list, name='debts-list'),

 
    
    
]
