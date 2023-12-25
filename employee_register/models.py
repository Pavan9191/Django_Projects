from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

def validator_field(value):
    if len(value) <= 4:
        raise ValidationError("Name must be greater than 4 characters ")


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullname = models.CharField(max_length=50, validators=[validator_field])
    emp_code = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
