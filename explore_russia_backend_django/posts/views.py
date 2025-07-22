import django.core.asgi
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action


class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["city", "title", "text"]
    ordering_fields = ["id", "city", "title"]

    @action(methods=["GET"], detail=False, serializer_class=PostSerializer)
    def last(self, request):
        queryset = Post.objects.all().order_by("-created_at")
        return Response([post.to_dict() for post in self.queryset][:9])
