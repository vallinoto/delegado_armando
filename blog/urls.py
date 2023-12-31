"""Module providing a site definition URLs."""
from django.urls import path
from members.views import PasswordsChangeView
from .views import HomeView, ArticleDetailView, AddPostView
from .views import AddCategoryView,UpdatePostView, DeletePostView
from .views import category_view


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add-post"),
    path('add_category/', AddCategoryView.as_view(), name="add-category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete-post"),
    path('category/<str:cats>/', category_view, name="category"),
    path('<int:pk>/password/',
         PasswordsChangeView.as_view(template_name='registration/change-password.html')),
]
