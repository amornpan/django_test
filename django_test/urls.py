"""
URL configuration for django_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
import django_test.views as views
from django.urls import re_path

urlpatterns = [
    #path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),


# parametoers in URL    
    path("search/<str:keyword>/<int:page>/", views.search, name="search"),

    path("date/<int:year>-<int:month>-<int:day>/", views.date, name="current_datetime"),

# Regex paths
    re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive, name="year_archive"),

    re_path(r"^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.month_archive, name="month_archive"),
]
