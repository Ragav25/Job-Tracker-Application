from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


appliedJobs =[
    {
        'role': 'Software Developer',
        'company': 'Precision IT Systems',
        'status': 'Pending',
        'date_applied': 'June 20'
    },
    {
        'role': 'Data Analytics',
        'company': 'Saber',
        'status': 'Pending',
        'date_applied': 'June 21'
    },


]

@login_required
def home(request):
    current_user = User.objects.filter(username=request.user)
    context = {
        'appliedJobs' : Post.objects.filter(author=current_user[0])
    }
    return render(request, 'sourceCode/home.html', context)


def about(request):
    return render(request, 'sourceCode/about.html', {'title': 'About'})
