
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.home_, name='home' ),
    path('', views.login_, name='login' ),
    path('dashboard/', views.dashboard_, name='dashboard' ),

    path('register/', views.register_, name='register' ),
]
