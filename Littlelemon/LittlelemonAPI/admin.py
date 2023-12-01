from django.contrib import admin
from .models import(
    MenuAPI,
    BookingAPI,
)


# Register your models here.
admin.site.register(BookingAPI)
admin.site.register(MenuAPI)