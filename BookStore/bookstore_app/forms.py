from django import forms
from .models import Cart


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ("title", "author", "cover_image", "price", "description")


# accounts/forms.py
from django import forms


class PasswordResetForm(forms.Form):
    email = forms.EmailField()
