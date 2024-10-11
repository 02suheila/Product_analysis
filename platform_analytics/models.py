from django.db import models

class FlipkartData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField("Email of the customer")
    platform = models.CharField("Platform",max_length=50)
    orders = models.IntegerField()
    returns = models.IntegerField()
    deliveries = models.IntegerField()

    class Meta:
        db_table = "flipkart_data"


class AmazonData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField("Email of the customer")
    platform = models.CharField("Platform",max_length=50)
    orders = models.IntegerField()
    returns = models.IntegerField()
    deliveries = models.IntegerField()

    class Meta:
        db_table = "amazon_data"
    
class AJIOData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField("Email of the customer")
    platform = models.CharField("Platform",max_length=50)
    orders = models.IntegerField()
    returns = models.IntegerField()
    deliveries = models.IntegerField()

    class Meta:
        db_table = "myjio_data"

class MyntraData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField("Email of the customer")
    platform = models.CharField("Platform",max_length=50)
    orders = models.IntegerField()
    returns = models.IntegerField()
    deliveries = models.IntegerField()

    class Meta:
        db_table = "myntra_data"