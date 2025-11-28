from django.db import models

class HOD(models.Model):
    Name=models.CharField()
    Pin=models.IntegerField()
    PH=models.BigIntegerField()

class Facality(models.Model):
    Name=models.CharField()
    Pin=models.IntegerField()
    PH=models.BigIntegerField()