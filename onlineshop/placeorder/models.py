from __future__ import unicode_literals

from django.db import models
from shop.models import Product
from django.utils.timezone import now

# Create your models here.
class Order(models.Model):
    firstName=models.CharField( unique=False, null=False)
    familyName=models.CharField( unique=False, null=False)
    email=models.EmailField()
    address=models.CharField(unique=False, null=False)
    zip=models.CharField(unique=False, null=False)#postal code
    city=models.CharField(unique=False, null=False)#postal code
    created=models.DateTimeField(default=now)
    updated=models.DateTimeField(default=now)
    paid=models.BooleanField(default=False)
    
    def __str__(self):
        return self.firstName
    def __unicode__(self):
        return self.firstName
    
    def getgetTotalCost(self):
        total=0
        for orderline in Orderline.objects.filter(order=self):
            total+=orderline.units*orderline.pricePerUnit
            
        

class Orderline(models.Model):
    order=models.ForeignKey(Order, related_name='orderLines', null=False)
    product=models.ForeignKey(Product, related_name='productLines', null=False)
    unit=models.IntegerField(default=0, null=False)
    pricePerUnit=models.DecimalField(decimal_places=2, max_digits=5)
    
    def __str__(self):
        return self.order + self.product
    def __unicode__(self):
        return self.order + self.product
    
    def getProductCost(self):
        return self.pricePerUnit
