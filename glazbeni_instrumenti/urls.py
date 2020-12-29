
from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', ImportData.as_view(), name='database'),
    path('index/', ForIndex.as_view(), name='index '),
]
