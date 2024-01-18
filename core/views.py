from django.shortcuts import render
from  book.models import PostModel
from category.models import CategoryModel

def homepage(request, category_slug=None):
    data  = PostModel.objects.all()
    categories = CategoryModel.objects.all()
    if category_slug is not None:
        category = CategoryModel.objects.get(slug = category_slug)
        data = PostModel.objects.filter(category = category)
    

    return render(request, 'index.html', {'data': data, 'categories': categories})
