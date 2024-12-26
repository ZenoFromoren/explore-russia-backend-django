"""
URL configuration for explore_russia_backend_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from posts.views import PostViewSet
from users.views import AuthViewSet, CustomTokenObtainPairView, UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from comments.views import CommentViewSet
from rest_framework_nested import routers


router = SimpleRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"users", UserViewSet, basename="users")
router.register(r"code", AuthViewSet, basename="code")

posts_router = routers.NestedSimpleRouter(router, r"posts", lookup="post")
posts_router.register(r"comments", CommentViewSet, basename="posts-comments")

comments_router = routers.NestedSimpleRouter(posts_router, r"comments", lookup="comment")
comments_router.register(r"replies", CommentViewSet, basename="comments-replies")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(posts_router.urls)),
    path("", include(comments_router.urls)),
    path("signin/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("admin/", admin.site.urls),
]
