from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.core.paginator import Paginator
from .models import ForumPost #Comment
# from .forms import CommentForm

# Create your views here.

class UserPost(View):
    forum_view = 'userforum.html'

    def get(self, request, *args, **kwargs):
        post_list = ForumPost.objects.order_by('-created_on')
        paginator = Paginator(post_list, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, self.forum_view, {"page_obj": page_obj})

# def userforum(request):
#     return render(request, 'userforum.html')


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
