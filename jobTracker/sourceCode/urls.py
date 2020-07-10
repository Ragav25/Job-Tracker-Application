from django.urls import path
from .views import (
                PostListView,
                PostDetailView,
                PostCreateView,
                PostUpdateView,
                PostDeleteView,
                # SearchListView
                )
from . import views

urlpatterns = [
    path('', views.home, name='jobTrack-home'),
    # path('', PostListView.as_view(), name='jobTrack-home'),
    path('job/advancesearch/', views.advance_search, name='jobTrack-advancesearch'),
    # path('job/search', SearchListView.as_view(), name='jobTrack-search'),

    path('job/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('job/new/', PostCreateView.as_view(), name='post-create'),
    path('job/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('job/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='jobTrack-about'),

]
