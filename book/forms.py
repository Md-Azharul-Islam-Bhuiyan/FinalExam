from django import forms
from book.models import  PostModel, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        exclude = ['posted_user']
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for field in self.fields:
             self.fields[field].widget.attrs.update({
                 'class':(
                    'd-block w-full bg-secondary-subtle'
                    'text-black border border-black rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-black'
                 )
             })

