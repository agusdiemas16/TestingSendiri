from django.contrib import admin

# Register your models here.
from cust.models import Customer, Vehicle

admin.site.register(Customer)
admin.site.register(Vehicle)