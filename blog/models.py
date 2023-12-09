"""Module providing a database structure."""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    '''
        Class name
    '''
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        '''
        Class name
        '''
        return reverse('home')
    

class Profile(models.Model):
    '''
        Class name
    '''
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    iniciation_date = models.DateField()
    elevation_date = models.DateField(null=True, blank=True)
    exaultation_date = models.DateField(null=True, blank=True)
    installation_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        '''
            Class name
        '''
        return str(self.user)


class Post(models.Model):
    '''
        Class name
    '''
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, default="TAG Default")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date  = models.DateField()
    category = models.CharField(max_length=255, default="Uncategorize")

    def __str__(self):
        '''
            Class name
        '''
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        '''
        Class name
        '''
        return reverse('home')
