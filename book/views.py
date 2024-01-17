from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import BookModel, Comment
from auth_user.models import ShopUserAccount
from .forms import BooksForm, CommentForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

@method_decorator(login_required, name='dispatch')
class AddBookView(CreateView):
    model = BookModel
    form_class = BooksForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('add_book')

    def form_valid(self, form):
        form.instance.posted_user = self.request.user
        messages.success(self.request, 'Book Successfully Added.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add Book'
        return context


@method_decorator(login_required, name='dispatch')
class EditBookView(UpdateView):
    model = BookModel
    form_class = BooksForm
    pk_url_kwarg = 'id'
    template_name = 'add_book.html'
    success_url = reverse_lazy('add_book')
    
    def form_valid(self, form):
        messages.success(self.request, 'Book Post Successfully Updated')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Edit Book'
        return context


@method_decorator(login_required, name='dispatch')
class DeleteBookView(DeleteView):
    model = BookModel
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

class DetailBookview(DetailView):
    model = BookModel
    pk_url_kwarg= 'id'
    template_name = 'details.html'
    
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        book = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object # post model er object ekhane store korlam
        comments = book.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context



@method_decorator(login_required, name='dispatch')
class EditCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    pk_url_kwarg = 'id'
    template_name = 'edit_comment.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Comment Successfully Updated')
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')    