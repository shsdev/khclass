"""khclass URL Configuration"""
from django.conf.urls import url
from django.contrib import admin
import os
from django.views.generic import RedirectView
import khclarifai.urls
from django.conf.urls import url, include


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='khclarifai:index')),
    url(r'^khclarifai/', include(khclarifai.urls, namespace="khclarifai")),
]
