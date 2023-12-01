from django.urls import path

from .views import(
    index,
    bookingView,
    menuView,
)


urlpatterns = [
    path("",index, name="index"),
    path("booking",bookingView, name="booking"),
    path("menu/",menuView,name="menu"),
    path("menu/<int:pk>",menuView,name="menu"),

]