from .models import TradingPost, Message
from crispy_forms.layout import Layout, Submit
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget
from django.core.validators import MaxLengthValidator, MinLengthValidator, FileExtensionValidator
from django.core.exceptions import ValidationError
from django import forms

def validate_image_size(image):
    max_size = 9 * 1024 * 1024  # 9MB
    if image.size > max_size:
        raise ValidationError('Image file too large ( > 9MB )')

class TradingPostForm(forms.ModelForm):
    title = forms.CharField(validators=[MinLengthValidator(2), MaxLengthValidator(200)])
    description = forms.CharField(widget=forms.Textarea, validators=[MinLengthValidator(5), MaxLengthValidator(750)])
    image = forms.ImageField(required=False, validators=[FileExtensionValidator(['jpg', 'png']), validate_image_size])
    class Meta:
        model = TradingPost
        fields = ['title', 'description', 'image', 'category', 'condition', 'status']
        widgets = {
            'image': forms.FileInput,
            'category': forms.RadioSelect,
            'condition': forms.RadioSelect,
            'status': forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super(TradingPostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'title', 
            'description', 
            'image', 
            'category', 
            'condition', 
            'status',
            Submit('submit', 'Create Post', css_class='btn btn-edit')
        )

        for field in self.fields.values():
            field.label = ''


class MessageForm(forms.ModelForm):
    text = forms.CharField(widget=SummernoteWidget(), required=True)

    class Meta:
        model = Message
        fields = ['text']