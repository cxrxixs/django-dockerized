from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("demo", views.demo, name="demo"),
    path("noresp", views.no_response, name="no-response"),
]
