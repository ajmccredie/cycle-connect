from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# from .models import Comment, ForumPost
# from .forms import CommentForm

# Create your views here.

# class UserPost(View):
#     def userforum(self, request, *args, **kwargs):
#         queryset = ForumPost.objects
#         post = get_object_or_404(queryset)
#         comments = post.comments.filter(approved=True).order_by('created_on')
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         comment_form = CommentForm(data=request.POST)

#         if comment_form.is_valid():
#             comment_form.instance.email = request.user.email
#             comment_form.instance.name = request.user.username
#             comment = comment_form.save(commit=False)
#             comment.save()

#         else:
#             comment_form = CommentForm()

#         return render(
#             request,
#             "userforum.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "commented": True,
#                 "liked": liked,
#                 "comment_form": CommentForm()
#             },
#         )

def userforum(request):
    return render(request, 'userforum.html')



