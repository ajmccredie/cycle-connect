from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.db.models import Q
from .models import ForumPost, Comment
from .forms import PostForm, CommentForm, SearchForm

# Create your views here.

class UserPost(LoginRequiredMixin, View):
    forum_view = 'userforum.html'

    def get(self, request, *args, **kwargs):
        post_list = ForumPost.objects.filter(published_status=1).order_by('-created_on')
        paginator = Paginator(post_list, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        liked_post_ids = set(request.user.likes.values_list('id', flat=True)) #Trying an idea from Stack Overflow
        form = PostForm()
        posts = ForumPost.objects.filter(published_status=1)
        return render(request, self.forum_view, {"page_obj": page_obj, "posts": posts, "form": form, "liked_post_ids": liked_post_ids})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.UserId_id = request.user.id
            new_post.save()
            return redirect('userforum') 
        else:
            post_list = ForumPost.objects.filter(published_status=1).order_by('-created_on')
            paginator = Paginator(post_list, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            liked_post_ids = set(request.user.likes.values_list('id', flat=True))
            posts = ForumPost.objects.filter(published_status=1)
            return render(request, self.forum_view, {"page_obj": page_obj, "posts": posts, "form": form, "liked_post_ids": liked_post_ids})


class PostLike(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(ForumPost, id=post_id)
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
            liked = True
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('userforum'))) # from a suggestion from Stack Overflow


class EditPost(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        post = get_object_or_404(ForumPost, id=post_id)

        if post.UserId != request.user:
            return redirect('userforum') # to catch any instances where the buttons displayed by mistake

        form = PostForm(instance=post)
        form.fields.pop('likes', None) # attempt to use 'pop' to remove the rogue likes list
        return render(request, 'edit_forum_post.html', {'form': form, 'post': post})

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        post = get_object_or_404(ForumPost, id=post_id)

        if post.UserId != request.user:
            return redirect('userforum') # to catch any instances where the buttons displayed by mistake

        form = PostForm(request.POST, instance=post)
        form.fields.pop('likes', None)
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

def edit_forum_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    if request.method =='POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('userforum_post_detail', post_id=post_id)
    else:
        form = CommentForm(instance=comment)
    context = {
        'form': form,
        'post_id': post_id
    }
    return render(request, 'edit_forum_comment.html', context) 
    

def delete_forum_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    if request.method == 'POST':
        comment.delete()
        return redirect('userforum_post_detail', post_id=post_id)
    else:
        context = {
            'comment': comment,
            'post_id': post_id,
            'comment_id': comment_id
        }
        return render(request, 'delete_forum_comment.html', context)


class SearchResultsView(LoginRequiredMixin, ListView):
    model = ForumPost
    template_name = 'forum_search.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            print(query)
            return ForumPost.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(UserId__username__icontains=query))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class ReportPostView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(ForumPost, pk=post_id)
        post.reported_status = 1
        post.published_status = 0
        post.reported_by.add(request.user)
        post.save()
        return redirect('userforum')
