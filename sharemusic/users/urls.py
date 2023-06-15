from django.urls import path, include
from .views import RegisterView,LoginView,Home,LogoutView
urlpatterns = [
    path('',Home,name = "home"),
    path('user/register/',RegisterView,name = "register"),
    path('user/login/',LoginView,name="login"),
    path('user/logout',LogoutView,name="logout"),
]
