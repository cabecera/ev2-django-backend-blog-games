from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list_get, name='api_products_list'),
    path('products/create/', views.product_create_post, name='api_products_create'),
    path('products/html/', views.list_products_view, name='products_html'),

]
