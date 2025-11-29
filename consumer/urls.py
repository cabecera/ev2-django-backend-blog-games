from django.urls import path
from core import views

urlpatterns = [
    path('products/', views.api_consumer_products, name='api_consumer_products'),
]
