from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', employee_form, name='employee_insert'),  # get and post request for insert operation
    path('<int:id>/', employee_form, name='employee_update'),  # get and post request for update operation
    path('delete/<int:id>/', employee_delete, name="employee_delete"), # get request to retrieve all records
    path('employee_list/', employee_list, name="employee_list")
]
