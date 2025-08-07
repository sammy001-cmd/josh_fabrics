from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Show index.html at /
    path('products/', views.product_list, name='product_list'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
]