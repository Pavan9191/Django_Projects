from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# bookstore/models.py
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='book_covers/')
    price = models.DecimalField(decimal_places=2, max_digits=8, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.user.username


# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
import uuid


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
