from django.urls import path
from . import views

app_name = "akademik"

urlpatterns = [
    path("", views.indexView, name="index"),
    path("<int:fakultas_id>", views.detailView, name="detail"),
    path("create/", views.createView, name="create"),
    path("update/<int:fakultas_id>", views.updateView, name="update"),
    path("delete/<int:fakultas_id>", views.deleteView, name="delete"),
]
