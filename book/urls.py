from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddBookView.as_view(), name='add_book'),
    path('edit/<int:id>', views.EditBookView.as_view(), name='edit_book'),
    path('delete/<int:id>', views.DeleteBookView.as_view(), name='delete_book'),
    path('details/<int:id>', views.DetailBookview.as_view(), name='detail_book'),
    path('editcomment/<int:id>', views.EditCommentView.as_view(), name='edit_comment'),
    path('deletecomment/<int:id>', views.DeleteCommentView.as_view(), name='delete_comment'),
]