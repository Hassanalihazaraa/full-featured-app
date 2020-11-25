from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreatView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreatView.as_view(), name='post-create'),
    path('about', views.about, name='about'),
]
