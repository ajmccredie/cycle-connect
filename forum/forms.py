from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import ForumPost, Comment
from django.core.validators import MaxLengthValidator, MinLengthValidator

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget(), required=True, validators=[MinLengthValidator(10, message="Content should be at least 10 characters long.")])
    class Meta:
        model = ForumPost
        fields = ['title', 'content', 'likes']
        widgets = {
            'content': SummernoteWidget(),
        }
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Please name your post'
        self.fields['title'].validators = [MaxLengthValidator(200, message="Title should be under 200 characters")]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = 'Write your comment here...'
            field.label = ''
            field.label_suffix = '' 


class SearchForm(forms.Form):
    query = forms.CharField()
