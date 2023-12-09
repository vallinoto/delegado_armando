"""Register models in the administrative page."""
from django.contrib import admin
from .models import Post, Category, Profile

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
