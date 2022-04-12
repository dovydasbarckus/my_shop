from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.EshopListView.as_view(), name='eshop'),
    path("store/", views.my_store, name="store"),
    path('register/', views.register, name='register'),
    path('shop/<int:pk>', views.ProductDetailView.as_view(), name='product')
]
