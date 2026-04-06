from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Owner(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cat = models.ForeignKey('Cat', on_delete=models.CASCADE, related_name='owners')

class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    birth_year = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='cats/', blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cats',
        null=True, blank=True  #
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        unique_together = ['name', 'owner']

    def __str__(self):
        return self.name