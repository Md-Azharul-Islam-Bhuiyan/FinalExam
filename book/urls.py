from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddPostView.as_view(), name='add_book'),
    path('edit/<int:id>', views.EditPostView.as_view(), name='edit_book'),
    path('delete/<int:id>', views.DeletePostView.as_view(), name='delete_book'),
    path('details/<int:id>', views.DetailPostview.as_view(), name='detail_book'),
    path('likepost/<int:id>', views.LikePostView, name='like'),
    path('dislikepost/<int:id>', views.DisLikePostView, name='dislike'),
    path('editcomment/<int:id>', views.EditCommentView.as_view(), name='edit_comment'),
    path('deletecomment/<int:id>', views.DeleteCommentView.as_view(), name='delete_comment'),
]