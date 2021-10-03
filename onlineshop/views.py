from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all().order_by('name')
    products = Product.objects.filter(available=True).order_by('?')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'onlineshop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'onlineshop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})


