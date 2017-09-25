"""khclass URL Configuration"""
from django.conf.urls import url
import os
import views

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'demo$', views.demo, name='demo'),
]
