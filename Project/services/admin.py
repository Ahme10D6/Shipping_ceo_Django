from django.contrib import admin
from .models import Addres, Customer, Shipping ,Company ,Tracking,Vehicle

# Register your models here.
admin.site.register(Shipping)
admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Tracking)
admin.site.register(Vehicle)
admin.site.register(Addres)