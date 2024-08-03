from django.urls import path
from .views import CommentCreateAPIView, CommentListAPIView, CommentDetailAPIView

urlpatterns = [
    path('post/<uuid:post_id>/comment', CommentCreateAPIView.as_view(), name='comment-create'),
    path('posts/<uuid:post_id>', CommentListAPIView.as_view(), name='comment-list'),
    path('<uuid:comment_id>', CommentDetailAPIView.as_view(), name='comment-detail'),
]
