from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    user1 = models.CharField(max_length=100, blank=True, null=True)
    user2 = models.CharField(max_length=100, blank=True, null=True)
    user3 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

