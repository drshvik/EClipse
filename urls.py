from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='post/login.html'),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('editprofile/',views.editprofile,name='editprofile'),
]
