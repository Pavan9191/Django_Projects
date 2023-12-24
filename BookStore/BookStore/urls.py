"""BookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from BookStore import settings
from bookstore_app.views import BookListView, Home, user_login, user_logout, admi, add_to_cart, view_cart, \
    delete_cart_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admi/', admi, name="admi"),
    path('', Home, name="home"),
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart', view_cart, name='view_cart'),
    path('delete_cart_item/<int:book_id>/',delete_cart_item,name='delete_cart_item'),
    path('list/', BookListView.as_view(), name='list'),

    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
