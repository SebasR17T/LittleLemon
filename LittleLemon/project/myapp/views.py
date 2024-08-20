from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


# Create your views here.

class ProductCreateView(CreateView):
    model : Product
    form_class = ProductForm
    template_name = 'productCreate.html'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'productUpdate.html'
    success_url = reverse_lazy('productList.html')

class ProductListView(ListView):
    model = Product
    template_name = 'productList.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'productDetail.html'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'productDelete.html'