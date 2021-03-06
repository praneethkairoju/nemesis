from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-home'),
    path('signup/', views.signuppage, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
]