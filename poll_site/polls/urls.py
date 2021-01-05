from django.urls import path
from . import views

urlpatterns = [
    # Home Page.
    path('', views.index, name="home"),
    
    # Create Poll Page
    path('create/', views.create, name="create_poll"),
    
    # To Test
]