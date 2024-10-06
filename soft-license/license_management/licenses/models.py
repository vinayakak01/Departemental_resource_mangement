from django.db import models

class OperatingSystem(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    license_type = models.CharField(max_length=50)
    date_purchased = models.DateField()
    valid_upto = models.DateField()
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class IDE(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    license_type = models.CharField(max_length=50)
    date_purchased = models.DateField()
    valid_upto = models.DateField()
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Software(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    license_type = models.CharField(max_length=50)
    date_purchased = models.DateField()
    valid_upto = models.DateField()
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name
