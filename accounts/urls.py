from django.urls import path
from . import views

urlpatterns = [
    path('register/editor/', views.register_editor, name='register_editor'),
    path('register/viewer/', views.register_viewer, name='register_viewer'),
]
