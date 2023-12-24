from django.contrib import admin

# Register your models here.
from bookstore_app.models import Book, UserProfile, Cart, PasswordReset

admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(PasswordReset)