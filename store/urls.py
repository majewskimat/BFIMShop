from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    # path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    # path ('about/', views.about, name="about"),
    # path ('contact/', views.contact, name="contact"),
    # path ('checkout/', views.checkout, name="checkout"),
]