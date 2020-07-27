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
from django.db.models import Q

def is_vaild_queryparam(param):
    return param != '' and param is not None

@login_required
def home(request):
    current_user = User.objects.filter(username=request.user)
    qs = Post.objects.filter(author=current_user[0], status__in=['pending', 'interviewing']).order_by('-date_applied')

    company_or_role_query = request.GET.get('company_or_role_contains')

    date_ascending = request.GET.get('date-asc')
    date_descending = request.GET.get('date-desc')
    company_ascending = request.GET.get('company-asc')
    company_descending = request.GET.get('company-desc')
    role_ascending = request.GET.get('role-asc')
    role_descending = request.GET.get('role-desc')

    if is_vaild_queryparam(company_or_role_query):
        qs = qs.filter(Q(company__icontains = company_or_role_query)
                    | Q(role__icontains = company_or_role_query)
                    ).distinct()

    if is_vaild_queryparam(date_ascending):
        qs = qs.order_by(date_ascending)

    if is_vaild_queryparam(company_descending):
        qs = qs.order_by(company_descending)

    if is_vaild_queryparam(company_ascending):
        qs = qs.order_by(company_ascending)

    if is_vaild_queryparam(role_descending):
        qs = qs.order_by(role_descending)

    if is_vaild_queryparam(role_ascending):
        qs = qs.order_by(role_ascending)

    if is_vaild_queryparam(role_descending):
        qs = qs.order_by(role_descending)

    context = {
        'appliedJobs' : qs
    }
    return render(request, 'sourceCode/home.html', context)

@login_required
def advance_search(request):
    qs_status = Post._meta.get_field('status')
    current_user = User.objects.filter(username=request.user)
    qs = Post.objects.filter(author=current_user[0]).order_by('-date_applied')

    company_contains_query = request.GET.get('company_contains')
    role_contains_query = request.GET.get('role_contains')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    status = request.GET.get('status')

    if is_vaild_queryparam(company_contains_query):
        qs = qs.filter(company__icontains=company_contains_query)

    if is_vaild_queryparam(role_contains_query):
        qs = qs.filter(role__icontains=role_contains_query)

    if is_vaild_queryparam(date_min):
        qs = qs.filter(date_applied__gte=date_min)

    if is_vaild_queryparam(date_max):
        qs = qs.filter(date_applied__lt=date_max)

    if is_vaild_queryparam(status) :
        qs = qs.filter(status=status)

    context = {
        'queryset' : qs,
        'qs_status' : qs_status
    }

    return render(request, 'sourceCode/advance_search.html', context)

def history(request):
    current_user = User.objects.filter(username=request.user)
    qs = Post.objects.filter(author=current_user[0], status='interviewing').order_by('-date_applied')

    qs_status = Post._meta.get_field('status')

    status = request.GET.get('value')

    if is_vaild_queryparam(status) :
        qs = Post.objects.filter(author=current_user[0], status=status).order_by('-date_applied')

    context = {
        'queryset' : qs,
        'qs_status' : qs_status
    }

    return render(request, 'sourceCode/history.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'sourceCode/home.html' # naming convention: <app>/<model>_<viewtype>/html
    context_object_name = 'appliedJobs'
    ordering = ['-date_applied']
    paginate_by = 5

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
