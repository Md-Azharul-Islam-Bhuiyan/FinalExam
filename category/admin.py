from django.contrib import admin
from .models import CategoryModel


class CategoryAdminModel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(CategoryModel,CategoryAdminModel)
