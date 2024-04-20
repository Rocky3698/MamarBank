from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER_TYPE

# Create your models here.
class Bank(models.Model):
    name=models.CharField(max_length=10, default='MamarBank',null=True,blank=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2,blank=True,null=True) 
    is_bankrupt = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name

class UserBankAccount(models.Model):
    Bank = models.ForeignKey(Bank,related_name='bank',on_delete=models.CASCADE,null=True,blank=True)
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True) # account no duijon user er kokhono same hobe na
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    initial_deposite_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2) # ekjon user 12 digit obdi taka rakhte parbe, dui doshomik ghor obdi rakhte parben 1000.50
    def __str__(self):
        return str(self.account_no)
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length= 50)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=50)
    def __str__(self):
        return str(self.user.email)
    