from django.db import models
from category.models import CategoryModel
from django.contrib.auth.models import User


class PostModel(models.Model):
    post_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="book/media/images/")
    category = models.ManyToManyField(CategoryModel, null=True, blank=True)
    posted_user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0) 
    dislike = models.IntegerField(default=0)
    description = models.TextField()
    
    def __str__(self):
        return self.post_name
    

class Comment(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE,related_name='comments',null=True, blank=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class LikePost(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    like_post = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} Liked {self.book.book_name}"
    
    class Meta:
        verbose_name_plural = "LikePosts"
    
class DisLikePost(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    dislike_post = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} DisLiked {self.book.book_name}"
    
    class Meta:
        verbose_name_plural = "DisLikePosts"





    