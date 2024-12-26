import django.urls
from rest_framework.serializers import ModelSerializer
from users.models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.forms.models import model_to_dict


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.city = validated_data.get("city", instance.city)
        instance.about = validated_data.get("about", instance.about)

        if validated_data.get("password"):
            instance.set_password(validated_data["password"])

        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "city",
            "about",
            "avatar",
            "email",
            "password",
            "date_joined",
        ]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = model_to_dict(self.user)
        return data
