from django.shortcuts import render
from .models import Post


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

def home(request):
    context = {
        'appliedJobs' : Post.objects.all()
    }
    return render(request, 'sourceCode/home.html', context)


def about(request):
    return render(request, 'sourceCode/about.html', {'title': 'About'})
