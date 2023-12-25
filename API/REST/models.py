from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.name, self.designation

