from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index),
    path("img/", views.Firm_Digital),
]
