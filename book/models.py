from django.db import models
from category.models import CategoryModel
from django.contrib.auth.models import User


class BookModel(models.Model):
    book_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="book/media/images/")
    category = models.ManyToManyField(CategoryModel, null=True, blank=True)
    posted_user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.book_name
    

class Comment(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE,related_name='comments',null=True, blank=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class BookOverView(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE,related_name='bookoverviews', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    like_post = models.IntegerField(default=0)
    dislike_post = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    