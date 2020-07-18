from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("create",views.create, name="create"),
    # path("random",views.random, name="random"),
    path("entries/<str:title>.md", views.css, name="css")
]
