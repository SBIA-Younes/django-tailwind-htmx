from django.shortcuts import render

from product.models import Product, Category

def frontpage(request):
  products = Product.objects.all()[0:8]
  
  return render(
    request, 
    'core/frontpage.html',
    {
      "products": products})
  
def shop(request):
  catagories = Category.objects.all()
  products = Product.objects.all()[0:8]

  active_category = request.GET.get('category', '')

  if active_category:
    products = Product.objects.filter(category__slug=active_category)
  
  return render(
    request, 
    'core/shop.html',
    {
      "products": products,
      "categories":catagories,
      'active_category':active_category,
      }
    )
