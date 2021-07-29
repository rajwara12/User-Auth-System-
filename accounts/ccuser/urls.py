 
from django.urls import path
from . import views

urlpatterns = [
    path( '', views.index,name="index"),
    path( 'handleSignup', views.handleSignup,name="handleSignup"),
    path( 'handleLogin', views.handleLogin,name="handleLogin"),
    path( 'handleLogout', views.handleLogout,name="handleLogout"),
    path('<auth_token>', views.verify, name="verify"),
    path( 'forget_pass/', views.forget_pass,name="forget_pass"),
    path('change_pass/<auth_token>/',views.change_pass, name="change_pass"),
]