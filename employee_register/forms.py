from django import forms
from .models import Employee
from django.forms import ValidationError


class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("fullname", "mobile", "emp_code", "position")
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'Emp code'
        }
        widgets = {
            'position': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(Employeeform, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'


'''
    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data["fullname"]
        if len(name) <= 4:
            raise forms.ValidationError("Name must be greater than 4 characters")
        return cleaned_data
'''
