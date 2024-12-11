from rest_framework.test import APITestCase
from django.urls import reverse
from posts.models import Post
import sys
from posts.serializers import PostSerializer
from rest_framework import status


class PostsApiTestCase(APITestCase):
    def setUp(self):
        self.post1 = Post.objects.create(
            id=1, city="Город 1", title="Город 1", image="https://link1.ru", text="Город 1"
        )
        self.post2 = Post.objects.create(
            id=2, city="Город 2", title="Город 2", image="https://link2.ru", text="Город 2"
        )
        self.post3 = Post.objects.create(
            id=3, city="Город 3", title="Город 3", image="https://link3.ru", text="Город 3"
        )

    def test_get(self):
        url = reverse("posts")

        response = self.client.get(url)
        serializer_data = PostSerializer(
            [self.post1, self.post2, self.post3], many=True
        ).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_by_id(self):
        url = reverse("postById", args=[2])

        response = self.client.get(url)
        serializer_data = PostSerializer(self.post2).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
