from django.contrib import admin
from .models import BookModel, BookOverView, Comment


admin.site.register(BookModel)
admin.site.register(BookOverView)
admin.site.register(Comment)
