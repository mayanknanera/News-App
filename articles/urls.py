# articles/urls.py
from django.urls import path
from .views import (
    ArticleListView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleCreateView,
)

urlpatterns = [
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("new/", ArticleCreateView.as_view(), name="article_create"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("", ArticleListView.as_view(), name="article_list"),
]
