from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import ForumPost, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content', 'likes']
        widgets = {
            'content': SummernoteWidget(),
        }
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Please name your post'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''
            field.label_suffix = '' 


class SearchForm(forms.Form):
    query = forms.CharField()
