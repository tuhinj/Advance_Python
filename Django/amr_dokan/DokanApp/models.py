from django.db import models
from accounts.models  import CustomUser

BRAND_CHOICES = [
    ('old', "OLD")
    ('new', 'NEW')
]

WARRANTY = [
    ('0', "No Warranty")
    ('1', "1 Month")
    ('2', "2 Month")
    ('3', "3 Month")
    ('4', "4 Month")
    ('5', "6 Month")
    ('6', "1 Year")
    ('7', "2 Month")
    ('10', "LifeTime")

]

# Create your models here.
class Ad(models, Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=)
    specifications = models.TextField()
    brand = models.CharField(max_length=20, null=True, blank=True)
    condition = models.CharField(choices=BRAND_CHOICES, max_length=3)
    color = models.CharField(max_length=20, null=True, blank=True)
    warranty = models.CharField(choices=WARRANTY, max_length=3)
    image1 = models.ImageField(upload_to="ads")
    image2 = models.ImageField(upload_to="ads", null=True, blank=True)
    image3 = models.ImageField(upload_to="ads", null=True, blank=True)
    image4 = models.ImageField(upload_to="ads", null=True, blank=True)
    cataegory
    location 
    seller = models.ForeignKey(CustomUser, related_name="ads")
    posited_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

