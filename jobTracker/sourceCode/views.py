from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
                            ListView,
                            DetailView,
                            CreateView,
                            UpdateView,
                            DeleteView
                            )
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .filters import PostFilters
from django.core.paginator import Paginator

@login_required
def home(request):
    current_user = User.objects.filter(username=request.user)
    context = {
        'appliedJobs' : Post.objects.filter(author=current_user[0])
    }

    return render(request, 'sourceCode/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'sourceCode/home.html' # naming convention: <app>/<model>_<viewtype>/html
    context_object_name = 'appliedJobs'
    ordering = ['-date_applied']
    paginate_by = 5


class SearchListView(ListView):
    model = Post
    template_name = 'sourceCode/search.html'

    def get_context_data(self, **kwargs):
        current_user = User.objects.filter(username=self.request.user)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilters(self.request.GET, queryset=Post.objects.filter(author=current_user[0]).order_by('-date_applied'))
        return context

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['company', 'role', 'status']
    success_url = reverse_lazy('jobTrack-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['company', 'role', 'status']
    success_url = reverse_lazy('jobTrack-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('jobTrack-home')

@login_required
def about(request):
    return render(request, 'sourceCode/about.html', {'title': 'About'})
