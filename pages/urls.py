from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='pages'),
    path('<int:pk>/', PostDetailView.as_view(), name='page-detail'),
    path('new/', PostCreateView.as_view(), name='page-create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='page-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='page-delete'),
]
