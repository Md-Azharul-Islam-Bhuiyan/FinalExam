from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from .models import PostModel, Comment, LikePost, DisLikePost
from auth_user.models import ShopUserAccount
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

@method_decorator(login_required, name='dispatch')
class AddPostView(CreateView):
    model = PostModel
    form_class = PostForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('add_book')

    def form_valid(self, form):
        form.instance.posted_user = self.request.user
        messages.success(self.request, 'Post Successfully Added.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add Post'
        return context


@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = PostModel
    form_class = PostForm
    pk_url_kwarg = 'id'
    template_name = 'add_book.html'
    success_url = reverse_lazy('add_book')
    
    def form_valid(self, form):
        messages.success(self.request, 'Book Post Successfully Updated')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Edit Post'
        return context


@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = PostModel
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

class DetailPostview(DetailView):
    model = PostModel
    pk_url_kwarg= 'id'
    template_name = 'details.html'
    
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

def LikePostView(request, id):
    book_obj = get_object_or_404(PostModel, id=id)
    
    if LikePost.objects.filter(post=book_obj, user=request.user).exists():
        print('You have already liked this post.')
        # return redirect('home')
    else:
        
        book_obj.like += 1
        book_obj.save()
        
        LikePost.objects.create(post=book_obj, user=request.user, like_post=1)
    return redirect('home')

def DisLikePostView(request, id):
    book_obj = get_object_or_404(PostModel, id=id)
    
    if DisLikePost.objects.filter(post=book_obj, user=request.user).exists():
            print('You have already liked this post.')
    else:
        
        book_obj.like += 1
        book_obj.save()
        
        DisLikePost.objects.create(post=book_obj, user=request.user, dislike_post=1)
    return redirect('home')
    
    

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