from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class PostsListApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["city", "title", "text"]
    ordering_fields = ["id", "city", "title"]


class PostsLastListApiView(ListAPIView):
    queryset = Post.objects.all().order_by("-createdAt")[:9]
    serializer_class = PostSerializer


class PostsDetailApiView(ListAPIView):
    def get_object(self, postId):
        try:
            return Post.objects.get(id=postId)
        except Post.DoesNotExist:
            return Response(status=404, message="Пост не найден")

    def get(self, requset, postId):
        post = self.get_object(postId)
        serializer = PostSerializer(post)

        return Response(serializer.data)
