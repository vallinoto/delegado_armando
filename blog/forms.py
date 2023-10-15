'''Module for forms definition'''
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    '''class name'''
    class Meta:
        '''class name'''
        model = Post
        fields = ('title','title_tag','author','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
            'author' : forms.Select(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'})
        }

class EditForm(forms.ModelForm):
    '''class name'''
    class Meta:
        '''class name'''
        model = Post
        fields = ('title','title_tag','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'})
        }
