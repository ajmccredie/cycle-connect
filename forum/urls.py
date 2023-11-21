from django.urls import path
from .views import UserPost, EditPost, DeletePost, like_post, userforum_post_detail

urlpatterns = [
    path('userforum/', UserPost.as_view(), name="userforum"),
    path('userforum/edit/<int:post_id>/', EditPost.as_view(), name='edit_forum_post'),
    path('userforum/delete/<int:post_id>/', DeletePost.as_view(), name='delete_forum_post'),
    path('userforum/like/<int:post_id>/', like_post, name='like_post'),
    path('userforum/detail/<int:post_id>/', userforum_post_detail, name='userforum_post_detail')
]