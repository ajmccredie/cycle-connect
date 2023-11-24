from django.urls import path
from .views import UserPost, EditPost, DeletePost, userforum_post_detail, PostLike, edit_forum_comment, delete_forum_comment

urlpatterns = [
    path('userforum/', UserPost.as_view(), name="userforum"),
    path('userforum/edit/<int:post_id>/', EditPost.as_view(), name='edit_forum_post'),
    path('userforum/delete/<int:post_id>/', DeletePost.as_view(), name='delete_forum_post'),
    path('userforum/like/<int:post_id>/', PostLike.as_view(), name='like_post'),
    path('userforum/detail/<int:post_id>/', userforum_post_detail, name='userforum_post_detail'),
    path('userforum/edit_comment/<int:post_id>/<int:comment_id>/', edit_forum_comment, name='edit_forum_comment'),
    path('userforum/delete_comment/<int:post_id>/<int:comment_id>/', delete_forum_comment, name='delete_forum_comment'),
]