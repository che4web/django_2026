"""
URL configuration for django2026 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from urlshortapp.views import ShortUrlsList, create_url, index, index_json, redirect_url

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("list", ShortUrlsList.as_view()),
    path("list_json", index_json),
    path("shortttt/<str:short_url>/", redirect_url, name="short-url"),
    path("form", create_url, name="create-url"),
]
