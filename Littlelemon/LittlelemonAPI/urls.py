from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import(
    bookingView,
    menuView,
)

urlpatterns = [
    path("auth-user",obtain_auth_token),
    path("booking",bookingView, name="booking"),
    path("menu-items/",menuView,name="menu"),
    path("menu-items/<int:pk>",menuView,name="menu-detail"),

]