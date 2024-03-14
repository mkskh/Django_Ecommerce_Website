from django.urls import path
from . import views


app_name = 'ecommerce'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
]