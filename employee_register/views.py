from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages

from employee_register.forms import Employeeform
from employee_register.models import Employee


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_list.html", context)


def employee_form(request, id=None):
    if request.method == "GET":
        if id is None:
            form = Employeeform()
        else:
            employee = Employee.objects.get(pk=id)
            form = Employeeform(instance=employee)

        return render(request, "employee_form.html", {'form': form})
    else:
        if id is None:
            form = Employeeform(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = Employeeform(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            messages.success(request, "Data saved successfully")
            return redirect('employee_insert')
        return render(request, "employee_form.html", {'form': form})


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')
