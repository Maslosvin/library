from django.db import models
# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    release_date = models.DateField()
    continuation_status = models.CharField(max_length=100)

class Order(models.Model):
    product = models.ManyToManyField('Product')
    pickup_point = models.CharField(max_length=100)
    receive_date = models.DateField()
    promo_code = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    email = models.EmailField()

class Reservation(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    reservation_date = models.DateField()