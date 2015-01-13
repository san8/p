from django.contrib import admin
from .models import Customer, Payment, Discount


admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Discount)
