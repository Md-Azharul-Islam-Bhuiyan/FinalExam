from django.contrib import admin
from .models import PostModel, Comment,LikePost, DisLikePost


admin.site.register(PostModel)
admin.site.register(Comment)
admin.site.register(LikePost)
admin.site.register(DisLikePost)
