from django.db import models

# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length=150)
    phoneNumber = models.IntegerField(max_length=50)
    date = models.DateField()
    typeOfPollution = models.CharField(max_length=150)
    detailDescription = models.TextField()

def _str_(self):
    return self.name
