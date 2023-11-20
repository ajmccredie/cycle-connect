from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import ForumPost

class PostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'please_name_your_post'


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('body',)