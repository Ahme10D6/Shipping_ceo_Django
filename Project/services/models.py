from django.db import models

# Create your models here.
class Shipping(models.Model):
    Shipping_id=models.IntegerField(primary_key=True,null=False)
    Shipping_name=models.CharField (max_length=20)
    Shipping_price=models.DecimalField (max_digits=10,decimal_places=2)
    Shipping_wight=models.DecimalField (max_digits=6,decimal_places=2)
    Shipping_hight=models.DecimalField (max_digits=6,decimal_places=2)
    Shipping_Breakable=models.BooleanField (default=None)
    Shipping_address=models.TextField ()
    Shipping_details=models.TextField ()
    
    def __str__(self):
        return self.Shipping_name

class Customer(models.Model):
    Customer_id=models.IntegerField(primary_key=True ,null=False)
    Customer_Email=models.EmailField()
    Customer_phone=models.DecimalField(max_digits=15,decimal_places=0)
    Customer_address=models.TextField()
    
    def __str__(self):
        return self.Customer_id

class Company(models.Model):
    Company_id=models.IntegerField(primary_key=True ,null=False)
    Company_name=models.CharField(max_length=20)
    Company_Email=models.EmailField()
    Company_phone=models.DecimalField(max_digits=15,decimal_places=0)
    Company_address=models.TextField()

    def __str__(self):
        return self.Company_name
   
class Tracking(models.Model):
    Tracking_id=models.IntegerField(primary_key=True ,null=False)
    Tracking_phone=models.DecimalField(max_digits=15,decimal_places=0)
    Tracking_address=models.TextField()
    Tracking_date=models.DateField()
    Package = models.OneToOneField(Shipping , on_delete=models.CASCADE ,verbose_name='shipping name')

    def __str__(self):
        return self.Tracking_id

class Vehicle(models.Model):
    Vehicle_id=models.IntegerField(primary_key=True ,null=False)
    Vehicle_model=models.DecimalField(max_digits=4,decimal_places=0)
    Vehicle_color=models.CharField(max_length=10)

class Addres(models.Model):
    Addres_contery=models.CharField(max_length=20)
    Addres_street=models.CharField(max_length=20)
    Addres_city=models.CharField(max_length=20)
    Addres_postalCode=models.DecimalField(max_digits=9,decimal_places=0)