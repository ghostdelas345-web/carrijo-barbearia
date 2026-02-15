from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class Service(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()  # Duration in minutes
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Configuration(models.Model):
    setting_name = models.CharField(max_length=255, unique=True)
    setting_value = models.TextField()