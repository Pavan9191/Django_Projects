from django.shortcuts import render, redirect

# Create your views here.
from portfolio.models import Project


def adm(request):
    return redirect('http://127.0.0.1:8000/admin/')


def home(request):
    return render(request, 'home.html')


def projects(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})


def project_detail(request, pk):
    projects = Project.objects.get(pk=pk)
    return render(request, 'details.html', {'project': projects})
