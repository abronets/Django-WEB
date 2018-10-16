from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .mixins import AddUserToFormMixin
from .forms import CreatePostForm, CreateCommentForm
from django.views.generic import *
from .models import Post, Comment


# Create your views here.


class IndexListView(ListView):
    paginate_by = 3
    template_name = "blog/index.html"
    queryset = Post.objects.all().order_by("published_date")
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = CreateCommentForm
        context['comment_url'] = reverse_lazy('comment_create', kwargs={'pk': self.kwargs['pk']})
        return context


class PostCreateView(AddUserToFormMixin, CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    success_url = '/posts/list'
    form_class = CreatePostForm


class PostUpdateView(AddUserToFormMixin, UpdateView):
    model = Post
    template_name = 'blog/create_post.html'
    success_url = '/posts/list'
    form_class = CreatePostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = '/posts/list'
    fields = '__all__'


class CommentCreateView(AddUserToFormMixin, CreateView):
    model = Comment
    form_class = CreateCommentForm
    template_name = 'blog/include/comment_create.html'
    success_url = '/'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['comment_url'] = reverse_lazy('comment_create', kwargs={'pk': self.kwargs['pk']})
        return context

    def form_valid(self, form):
        new_form = form.save(commit=False)
        new_form.user = self.request.user
        new_form.post_id = self.kwargs['pk']
        new_form.save()
        return HttpResponseRedirect(self.get_success_url())


class CommentUpdateView(AddUserToFormMixin, UpdateView):
    model = Comment
    form_class = CreateCommentForm
    template_name = 'blog/include/comment_create.html'
    success_url = '/'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_id']})

    def get_context_data(self, **kwargs):
        context = super(CommentUpdateView, self).get_context_data(**kwargs)
        context['comment_url'] = reverse_lazy(
            'comment_update', kwargs={'pk': self.object.id, 'post_id': self.object.post.id}
        )
        return context

    def form_valid(self, form):
        new_form = form.save(commit=False)
        new_form.user = self.request.user
        new_form.post_id = self.kwargs['post_id']
        new_form.save()
        return HttpResponseRedirect(self.get_success_url())
