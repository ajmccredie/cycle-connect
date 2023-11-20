from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.core.paginator import Paginator
from .models import ForumPost #Comment
from .forms import PostForm #CommentForm

# Create your views here.

class UserPost(LoginRequiredMixin, View):
    forum_view = 'userforum.html'

    def get(self, request, *args, **kwargs):
        # post_list = ForumPost.objects.order_by('-created_on')
        # paginator = Paginator(post_list, 8)
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        posts = ForumPost.objects.all()
        form = PostForm()

        return render(request, self.forum_view, {"posts": posts, "form": form})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.UserId_id = request.user.id
            new_post.save()
            return redirect('userforum') 
        else:
            posts = ForumPost.objects.all()
            return render(request, self.forum_view, {'posts': posts, 'form': form})

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
