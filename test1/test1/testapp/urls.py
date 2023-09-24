
from django.urls import path
from . import views 

urlpatterns = [
 
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('cars_specifications/<id>', views.cars_specifications, name="cars_specifications"),
    path('category_products/<id>', views.category_products, name="category_products"),
    path('contact/', views.contact, name="contact"),
    path('subscribe/', views.subscribe, name='subscribe'),
]