from django.db import models


class Leadership(models.Model):
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    number = models.IntegerField()
    email = models.EmailField()
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name


class Structural(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name