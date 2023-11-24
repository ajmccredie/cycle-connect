from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from .models import ForumPost, Comment
from .forms import PostForm, CommentForm

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


class PostLike(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(ForumPost, id=post_id)
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
            liked = True
        return HttpResponseRedirect(reverse('userforum'))


class EditPost(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        post = get_object_or_404(ForumPost, id=post_id)

        if post.UserId != request.user:
            return redirect('userforum') # to catch any instances where the buttons displayed by mistake

        form = PostForm(instance=post)
        return render(request, 'edit_forum_post.html', {'form': form, 'post': post})

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        post = get_object_or_404(ForumPost, id=post_id)

        if post.UserId != request.user:
            return redirect('userforum') # to catch any instances where the buttons displayed by mistake

        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('userforum')
        else:
            return render(request, 'edit_forum_post.html', {'form': form, 'post': post})


class DeletePost(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        post = get_object_or_404(ForumPost, id=post_id)

        if post.UserId != request.user:
            return redirect('userforum')
        
        return render(request, 'delete_forum_post.html', {'post': post})

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        post = get_object_or_404(ForumPost, id=post_id)

        if post.UserId == request.user:
            post.delete()
            return redirect('userforum')
        else:
            return redirect('userforum')

def userforum_post_detail(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    comments = post.comments.all()
    new_comment = None
    comment_form = CommentForm()
    if request.method == 'POST': 
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user
            new_comment.UserId_id = request.user.id
            new_comment.save()
            return redirect('userforum_post_detail', post_id=post_id)
    else:
        comment_form = CommentForm()
    return render(request, "userforum_post_detail.html", {"post": post, "comments": comments, "new_comment": new_comment, "comment_form": comment_form})

        