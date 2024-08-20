from django.urls import path
from . import views
from .views import ProductCreateView, ProductUpdateView, ProductListView, ProductDeleteView, ProductDetailView

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name="createProduct"),
    path('update/<int:pk>', ProductUpdateView.as_view(), name="updateProduct"),
    path('list/', ProductListView.as_view(), name="listProduct"),
    path('delete<int:pk>/', ProductDeleteView.as_view(), name="deleteProduct"),
    path('detail/<int:pk>', ProductDetailView.as_view(), name="detailProduct")

]