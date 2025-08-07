
# from django.shortcuts import render
# from .models import Product

# def product_list(request):
#     products = Product.objects.filter(is_available=True)
#     return render(request, 'store/index.html', {'products': products})


from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request):
    return render(request, 'store/index.html')

def product_list(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'store/product_list.html', {'products': products})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category_product.html', {
        'category': category,
        'products': products
    })