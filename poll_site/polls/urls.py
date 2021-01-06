from django.urls import path
from . import views

urlpatterns = [
    # Home Page.
    path('', views.index, name="home"),
    
    # Create Poll Page.
    path('create/', views.create, name="create_poll"),
    
    # Vote Page.
    path('vote/<int:poll_id>', views.vote, name="vote"),
    
    # Delete Poll.
    path('delete/<int:poll_id>', views.delete_poll, name='delete_poll'),
    
    # Result Page.
    path('result/<int:poll_id>', views.result, name='result'),
    
    # Result data for a Chart.
    path('resultdata/<int:obj>', views.result_data, name="result_data"),
]