from django.urls import path
from . import views

urlpatterns = [
    path ('', views.store, name="store"),
    path ('about/', views.about, name="about"),
    path ('contact/', views.contact, name="contact"),
    path ('checkout/', views.checkout, name="checkout"),
]