from django.urls import path
from .views import PostsListApiView, PostsLastListApiView, PostsDetailApiView


urlpatterns = [
    path("", PostsListApiView.as_view(), name="posts"),
    path("last/", PostsLastListApiView.as_view(), name="lastPosts"),
    path("<int:postId>/", PostsDetailApiView.as_view(), name="postById")
]
