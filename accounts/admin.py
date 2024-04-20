from django.contrib import admin
from .models import UserAddress,UserBankAccount,Bank
# Register your models here.
admin.site.register(UserAddress)
admin.site.register(UserBankAccount)
admin.site.register(Bank)