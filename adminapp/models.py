from django.db import models

# Create your models here.
class SignUpData(models.Model):
    sign_name=models.CharField(max_length=100,blank=False)
    sign_email=models.EmailField(max_length=100,blank=False,unique=True)
    sign_password=models.CharField(max_length=100, blank=False)
    sign_time= models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.sign_name
    class Meta:
        db_table="users_data"

class ForgotPassword(models.Model):
    email=models.EmailField(blank=False)
    class Meta:
        db_table="forgotpassword"
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    category_choices = (("Dog", "Dog"), ("Cat", "Cat"), ("Bird", "Bird"), ("Fish","Fish"),("Rabbit","Rabbit"),("Gunniepig","Gunniepig"))
    category = models.CharField(max_length=100, blank=False,choices=category_choices)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200,blank=False)
    price = models.PositiveIntegerField(blank=False)
    image = models.FileField(blank=False,upload_to="productimages")
    secure_key = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "product_table"

class Owners(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=50,blank=False)
    secure_key = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.username
    class Meta:
        db_table = "owners_table"