from django.urls import path
from .views import UserPost, EditPost, DeletePost, ForumPostDetailView, PostLike, EditForumCommentView, DeleteForumCommentView, SearchResultsView, ReportPostView

urlpatterns = [
    path('userforum/', UserPost.as_view(), name="userforum"),
    path('userforum/edit/<int:post_id>/', EditPost.as_view(), name='edit_forum_post'),
    path('userforum/delete/<int:post_id>/', DeletePost.as_view(), name='delete_forum_post'),
    path('userforum/like/<int:post_id>/', PostLike.as_view(), name='like_post'),
    path('userforum/detail/<int:pk>/', ForumPostDetailView.as_view(), name='userforum_post_detail'),
    path('userforum/edit_comment/<int:pk>/', EditForumCommentView.as_view(), name='edit_forum_comment'),
    path('userforum/delete_comment/<int:pk>/<int:comment_id>/', DeleteForumCommentView.as_view(), name='delete_forum_comment'),
    path('userforum/forum_search/', SearchResultsView.as_view(), name='forum_search'),
    path('userforum/report_post/<int:post_id>/', ReportPostView.as_view(), name='report_post'),
]