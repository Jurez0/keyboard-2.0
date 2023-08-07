from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
#from .models import Product, PCB, Switch, Keyboard, KeyCap
from .models import Category, Item

def product_all(request):
	# query = request.GET.get('query', '')
    # category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    
    return render(request, 'catalog/index.html', {
        'items': items,
        # 'query': query,
        'categories': categories,
        # 'category_id': int(category_id)
    })


















# def product_all(request):
#     products = Product.objects.all().select_related('content_type')
#     categories = {'pcb','switch', 'keyboard', 'keycap'}

#     return render(request, 'catalog/index.html', {'products': products, 'categories': categories})



# def product_filtered(request):
# 	categ=request.GET.getlist('type[]')
# 	categories = {'pcb','switch', 'keyboard', 'keycap'}
# 	products=Product.objects.all().select_related('content_type')
# 	if len(categ)>0:
# 		products=Product.objects.all().filter(content_type=categ).select_related('content_type')
	
# 	return render(request,'catalog/filter_index.html', {'products': products,})