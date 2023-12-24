from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.db.models import Q
from .models import ForumPost, Comment
from .forms import PostForm, CommentForm, SearchForm


# See and add posts
class UserPost(LoginRequiredMixin, View):
    template_name = 'forum/userforum.html'
    paginate_by = 8

    def get(self, request, *args, **kwargs):
        user = request.user
        post_list = ForumPost.objects.filter(
            Q(published_status=1) | Q(UserId=user, published_status=0)
        ).order_by('-created_on')
        paginator = Paginator(post_list, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "page_obj": page_obj,
            "form": PostForm(),
            "liked_post_ids": set(user.likes.values_list('id', flat=True)) if user.is_authenticated else set()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.UserId = request.user
            new_post.save()
            return redirect('userforum')
        else:
            user = request.user
            post_list = ForumPost.objects.filter(
                Q(published_status=1) | Q(UserId=user, published_status=0)
            ).order_by('-created_on')
            paginator = Paginator(post_list, self.paginate_by)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context = {
                "page_obj": page_obj,
                "form": form,
                "liked_post_ids": set(user.likes.values_list('id', flat=True)) if user.is_authenticated else set()
            }

            return render(request, self.template_name, context)


# Like posts on the forum
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


# Edit posts
class EditPost(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        post = get_object_or_404(ForumPost, id=post_id)

        if post.UserId != request.user:
            return redirect('userforum') # to catch any instances where the buttons displayed by mistake

        form = PostForm(instance=post)
        form.fields.pop('likes', None) # attempt to use 'pop' to remove the rogue likes list
        return render(request, 'forum/edit_forum_post.html', {'form': form, 'post': post})

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
            return render(request, 'forum/edit_forum_post.html', {'form': form, 'post': post})


# Delete posts
class DeletePost(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        post = get_object_or_404(ForumPost, id=post_id)

        if post.UserId != request.user:
            return redirect('userforum')
        
        return render(request, 'forum/delete_forum_post.html', {'post': post})

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        post = get_object_or_404(ForumPost, id=post_id)

        if post.UserId == request.user:
            post.delete()
            return redirect('userforum')
        else:
            return redirect('userforum')


# View greater detail about a post and comment
class ForumPostDetailView(DetailView, LoginRequiredMixin):
    model = ForumPost
    template_name = "forum/userforum_post_detail.html"
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all()
        context['new_comment'] = None
        context['comment_form'] = CommentForm()
        context['post_reported'] = post.reported_status == 1
        context['post_id'] = post.id
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user
            new_comment.UserId_id = request.user.id
            new_comment.save()
        return redirect('userforum_post_detail', pk=post.pk)


# Edit the comment
class EditForumCommentView(UpdateView, LoginRequiredMixin):
    model = Comment
    form_class = CommentForm
    template_name = "forum/edit_forum_comment.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return render(request, self.template_name, {'form': form, 'post': self.object.post})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect('userforum_post_detail', pk=self.object.post.id)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form, 'post': self.object.post})
    

# Delete the comment
class DeleteForumCommentView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'forum/delete_forum_comment.html'

    def get_success_url(self):
        return reverse('userforum_post_detail', kwargs={'pk': self.object.post.pk})

    def get_object(self, queryset=None):
        comment_id = self.kwargs.get('comment_id')
        return get_object_or_404(Comment, id=comment_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.object.post.id
        context['comment_id'] = self.object.id
        return context


# Search the forum posts
class SearchResultsView(LoginRequiredMixin, ListView):
    model = ForumPost
    template_name = 'forum/forum_search.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            print(query)
            return ForumPost.objects.filter((Q(title__icontains=query) | Q(content__icontains=query) | Q(UserId__username__icontains=query)) & Q(published_status=1)) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


# Report forum posts
class ReportPostView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        print("Debug code")
        print(post_id)
        post = get_object_or_404(ForumPost, pk=post_id)
        post.reported_status = 1
        post.published_status = 0
        post.reported_by.add(request.user)
        print(post.published_status)
        post.save()
        return redirect('userforum')
