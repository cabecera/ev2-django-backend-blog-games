from django.urls import path
from . import views

app_name = 'comunidad'

urlpatterns = [
    path('', views.comunidad, name='comunidad'),
]

