""" url """
from django.conf.urls import url, include
from .views import LoginView, BlogView, RegisterView
from rest_framework import routers



urlpatterns = [
    url(r'^login/$', LoginView.as_view()),
    url(r'^register/$', RegisterView.as_view()),
    url(r'^blog/$', BlogView.as_view())
]
