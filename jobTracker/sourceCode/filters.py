import django_filters
from .models import Post


class PostFilters(django_filters.FilterSet):

    class Meta:
        model = Post
        fields = {
            'company': ['icontains'],
            'role': ['icontains'],
            'status': ['icontains']
        }
