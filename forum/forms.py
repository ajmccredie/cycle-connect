from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import ForumPost, Comment
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Form to allow users to post and edit their posts
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


# Form to allow users to comment and edit their comments
class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, validators=[MaxLengthValidator(500, message="Comment should be under 500 characters")])
    class Meta:
        model = Comment
        fields = ('body',)
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['placeholder'] = 'Write your comment here...'
        self.fields['body'].label = ''
        self.fields['body'].label_suffix = '' 


# Form to allow users to search the posts on the forum
class SearchForm(forms.Form):
    query = forms.CharField(
        validators=[MaxLengthValidator(100, message="Search query should be under 100 characters")],
        widget=forms.TextInput(attrs={'maxlength': '100'})  
    )