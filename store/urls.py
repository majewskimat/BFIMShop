from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path ('about/', views.about, name='about'),
    path ('contact/', views.contact, name='contact'),
    path ('payment/ordercompleted/', views.order_completed, name='order_completed'),
    path('contact/contactsuccess/', views.contact_success, name='contact_success'),
]