from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import User
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer
from django.forms.models import model_to_dict
from rest_framework.views import APIView
import random
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.conf import settings


def generate_code():
    return str(random.randint(0, 9999)).zfill(4)


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["GET", "PATCH"], detail=False, serializer_class=UserSerializer)
    def me(self, request):
        if request.method == "PATCH":
            pk = request.user.id

            if not pk:
                return Response({"error": "Method PATCH not allowed"})

            try:
                instance = User.objects.get(pk=pk)
            except:
                return Response({"error": "Object doesnt exist"})

            update_user_data = {
                "username": request.data.get("username", instance.username),
                "email": instance.email,
                "password": request.data.get("password", instance.password),
                **request.data,
            }

            serializer = UserSerializer(data=update_user_data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)

        return Response(model_to_dict(User.objects.get(id=request.user.id)))


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class AuthViewSet(viewsets.ViewSet):
    @action(methods=["POST"], detail=False)
    def confirm_registration(self, request):
        code = generate_code()

        html_content = render_to_string(
            "confirm_registration_email.html",
            context={"username": request.data["username"], "code": code},
        )

        send_mail(
            subject="Подтверждение рагистрации на explore-russia.ru",
            message="",
            from_email=settings.EMAIL_HOST,
            recipient_list=[request.data["email"]],
            html_message=html_content,
        )

        return Response({"user": request.data, "code": code})

    @action(methods=["POST"], detail=False)
    def reset_password(self, request):
        code = generate_code()

        html_content = render_to_string(
            "reset_password_email.html",
            context={"username": request.user.username, "code": code},
        )

        send_mail(
            subject="Сброс пароля на explore-russia.ru",
            message="",
            from_email=settings.EMAIL_HOST,
            recipient_list=[request.user.email],
            html_message=html_content,
        )

        return Response({"user": model_to_dict(request.user), "code": code})
