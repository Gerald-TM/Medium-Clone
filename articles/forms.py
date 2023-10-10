from .models import Article
from django import forms

class ArticleCreateForm(forms.ModelForm):
    title = forms.CharField( widget=forms.TextInput (attrs={
        'placeholder': 'Title',
        # 'value': 'giig'
        

    }))
    body = forms.CharField (label='', widget=forms.Textarea (attrs={
        'class': 'article-create-form-body', 
        'placeholder': 'Tell your story...',
    

    }))
    class Meta:
        model = Article
        fields = [
            'title', 
            'body'
        ]
