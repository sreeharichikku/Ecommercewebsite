from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)


class Productss(models.Model):
    image = models.ImageField(upload_to='images', max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    Discription = models.TextField()
    price = models.CharField(max_length=255)
    sale_price = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name


class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Productss, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True, null=True)
    update_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.username
