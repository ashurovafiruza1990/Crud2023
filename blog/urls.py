from django.urls import path
from .views import article_func, article_detail, article_create, article_edit, article_delete, like_article, dislike_article, delete_comment, comment_edit

urlpatterns= [
    path('', article_func, name='article_func'),
    path('<slug>', article_detail, name='article_detail'),
    path('article_create/', article_create, name='article_create'),
    path('article_edit/<slug>', article_edit, name='article_edit'),
    path('article_delete/<slug>', article_delete, name='article_delete'),
    path('<slug>/like', like_article, name='like_article'),
    path('<slug>/diclike', dislike_article, name='dislike_article'),
    path('<slug>/comment/<int:pk>/delete_comment', delete_comment, name='delete_comment'),
    path('<slug>/comment/<int:pk>/coment_edit', comment_edit, name='comment_edit'),
]