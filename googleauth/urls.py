from django.urls import path

from .views import *
urlpatterns = [
    path('init/', request),
    path('redirect/', redirect)
]