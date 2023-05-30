from django.contrib.auth import views as auth_views
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.home_, name='home' ),
    path('', views.login_, name='login' ),
    path('dashboard/', views.dashboard_, name='dashboard' ),
    path('register/', views.register_, name='register' ),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complate" ),
]
