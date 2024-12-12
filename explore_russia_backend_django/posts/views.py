from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from django.forms.models import model_to_dict


class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["city", "title", "text"]
    ordering_fields = ["id", "city", "title"]

    @action(methods=['GET'], detail=False, serializer_class=PostSerializer)
    def last(self, request):
        queryset = Post.objects.all()
        return Response([model_to_dict(post) for post in queryset][:9])


# class PostsListApiView(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ["city", "title", "text"]
#     ordering_fields = ["id", "city", "title"]


# class PostsLastListApiView(ListAPIView):
#     queryset = Post.objects.all().order_by("-createdAt")[:9]
#     serializer_class = PostSerializer


# class PostsDetailApiView(ListAPIView):
#     def get_object(self, postId):
#         try:
#             return Post.objects.get(id=postId)
#         except Post.DoesNotExist:
#             return Response(status=404, message="Пост не найден")

#     def get(self, requset, postId):
#         post = self.get_object(postId)
#         serializer = PostSerializer(post)

#         return Response(serializer.data)
