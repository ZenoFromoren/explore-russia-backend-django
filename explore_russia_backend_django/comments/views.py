from rest_framework import mixins, viewsets
from comments.models import Comment
from comments.serializers import CommentSerializer
from posts.models import Post
from users.models import User
from rest_framework.response import Response
from django.forms.models import model_to_dict


class CommentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer

    def create(self, request, post_pk=None):
        comment = Comment.objects.create(
            text=request.data["text"],
            owner=User.objects.get(id=request.user.id),
            post=Post.objects.get(id=post_pk),
            parent=Comment.objects.get(id=request.data["parent"]) if request.data["parent"] else None,
        )
        comment.save()
        return Response(model_to_dict(comment))

    def list(self, request, post_pk=None, comment_pk=None):
        if comment_pk:
            comments = self.queryset.filter(post=post_pk, parent=comment_pk)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        comments = self.queryset.filter(post=post_pk, parent=None)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
