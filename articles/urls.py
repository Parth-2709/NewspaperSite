from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleUpdateView,
    ArticleCreateView,
    CommentCreateView,
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('create/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/new_comment/', CommentCreateView.as_view(), name='comment_new'),
]