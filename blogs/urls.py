from django.urls import path
from .views import BlogCreateAPIView,BlogDetailUpdateDeleteAPIView, BlogListAPIView, BlogDetailAPIView


urlpatterns = [
    path('create', BlogCreateAPIView.as_view(), name='blog-list'),
    path('list', BlogListAPIView.as_view(), name='blog-list'),
    path('<uuid:blog_id>/detail', BlogDetailAPIView.as_view(), name='blog-details'),
    path('<uuid:blog_id>', BlogDetailUpdateDeleteAPIView.as_view(), name='blog-update-delete'),
]