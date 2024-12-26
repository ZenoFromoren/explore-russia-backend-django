from rest_framework.serializers import ModelSerializer
from comments.models import Comment
from posts.models import Post
from users.models import User
from django.forms.models import model_to_dict


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def update(self, instance, validated_data):
        super(CommentSerializer, self).update(instance, validated_data)
        if not instance.is_edited:
            instance.is_edited = True
        instance.save()
        return instance

    def to_representation(self, instance):
        rep = super(CommentSerializer, self).to_representation(instance)
        rep["owner"] = model_to_dict(instance.owner)
        rep["replies"] = [
            self.to_representation(reply)
            for reply in instance.replies.all().order_by(("created_at"))
        ]
        return rep
