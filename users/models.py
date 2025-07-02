from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    Role_Choices = [
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    ]

    role = models.CharField(max_length=10, choices=Role_Choices, default='employee')
    position = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
