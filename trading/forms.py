from .models import TradingPost
from crispy_forms.layout import Layout, Submit
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django import forms


class TradingPostForm(forms.ModelForm):
    class Meta:
        model = TradingPost
        fields = ['title', 'description', 'image', 'category', 'condition', 'status']
        widgets = {
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
        self.label_suffix = ""
        for field in self.fields:
            self.fields[field].label_suffix = ""
