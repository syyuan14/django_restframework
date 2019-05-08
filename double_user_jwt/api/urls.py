from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .views import TestView
urlpatterns = [
    url(r'^login/$', obtain_jwt_token),
    url(r'^test/$', TestView.as_view())
]
