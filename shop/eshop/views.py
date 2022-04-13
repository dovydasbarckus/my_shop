from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView

from .models import Customer, Order, Product, ProductOrder, Status
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import User


def my_store(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user)
        items = order.productorder_set.all()
    else:
        items = []
        order = {'get_all_items': 0, 'get_cart_total': 0}

    context = {'order': order, 'items': items}
    return render(request, 'my_store.html', context)


class EshopListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'eshop.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product.html'


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username: {username} already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'User with this email: {email} already exists!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    return render(request, 'registration/register.html')

