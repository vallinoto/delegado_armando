'''Module for forms definition'''
from django import forms
from .models import Post, Category


cats = Category.objects.all().values_list('name', 'name')
cats_list = []
for cat in cats:
    cats_list.append(cat)

class PostForm(forms.ModelForm):
    '''class name'''
    class Meta:
        '''class name'''
        model = Post
        fields = ('title','title_tag','author','category','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
            'author' : forms.TextInput(attrs={'class' : 'form-control', 'value':'', 'id':'author_id', 'type':'hidden'}),
            #'author' : forms.Select(attrs={'class' : 'form-control'}),
            'category' : forms.Select(choices=cats_list, attrs={'class' : 'form-control'}),
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
