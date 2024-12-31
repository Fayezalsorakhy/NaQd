from django.urls import path     
from . import views
urlpatterns = [
    path('', views.login),   
    path('register', views.register), 
    path('main', views.main,name="main"),
    path('api/customers/', views.customers_list, name='customers-list'),
    path('api/debts/', views.debts_list, name='debts-list'),
    path('delete_debt/<int:pk>/', views.delete_debt, name='delete_debt'),
    path('select_customer/', views.select_customer, name='select_customer'),
    path('customers_view', views.customers_view, name='customers_view'),
    
    path('add_debts/', views.add_debts, name='add_debts'),
    
    
    
    
    
    
    
    

    
    

 
    
    
]
