"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from website.views import basic_login, print_products, add_product, create_account, delete_account, get_account_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # new,
    # path("inputTest1", basic_login, name='basic_login'),

    path("user/signin", basic_login, name='basic_login'),
    path("user/create", create_account, name = 'create_account'),
    path("user/delete", delete_account, name = 'delete_account'),
    path("user", get_account_info, name = 'get_account_info'),


    path('products/list', print_products, name = 'print_products'),

    path('products/add', add_product, name = 'add_product'),


]
