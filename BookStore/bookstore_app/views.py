from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
# In the Django shell
from django.contrib.auth.models import User
from django.urls import reverse

from .models import UserProfile, PasswordReset
import smtplib

for user in User.objects.all():
    UserProfile.objects.get_or_create(user=user)

# Create your views here.
# bookstore/views.py
from django.views.generic import ListView
from .models import Book, UserProfile, Cart


def Home(request):
    return redirect('list')


def admi(request):
    return redirect('http://127.0.0.1:8000/admin/login/?next=/admin/')


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('list')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('list')


def add_to_cart(request, book_id):
    if user.is_authenticated:
        book = Book.objects.get(pk=book_id)
        # user_profile = request.user.userprofile
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.books.add(book)
        return redirect('view_cart')
    else:
        return redirect("home")


def view_cart(request):
    # user_profile = request.user.userprofile
    if user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        books = cart.books.all()
        return render(request, 'cart.html', {'cart': books})


def delete_cart_item(request, book_id):
    # user_profile = request.user.userprofile
    if user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        book = get_object_or_404(Book, pk=book_id)

        # Remove the book from the cart
        cart.books.remove(book)

        return redirect('view_cart')

