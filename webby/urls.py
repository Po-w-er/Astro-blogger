from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostDeleteView, PostUpdateView, UserPostListView
from webby.views import about

urlpatterns = [
   path('', PostListView.as_view(), name='webby-home'),
   path('my-post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   path('my-post/<int:pk>/update/', PostUpdateView.as_view(), name='update-post'),
   path('my-post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
   path('create-post/', PostCreateView.as_view(), name='new-post'),
   path('about/',about, name='about')
]
