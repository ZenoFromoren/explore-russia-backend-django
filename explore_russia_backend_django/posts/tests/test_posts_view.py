from rest_framework.test import APITestCase
from django.urls import reverse
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import status
from posts.views import PostViewSet
from django.http import HttpRequest


class PostsApiTestCase(APITestCase):
    def setUp(self):
        self.post1 = Post.objects.create(
            id=1,
            city="Город 1",
            title="Город 1",
            image="https://link1.ru",
            text="Город 1",
        )
        self.post2 = Post.objects.create(
            id=2,
            city="Город 2",
            title="Город 2",
            image="https://link2.ru",
            text="Город 2",
        )
        self.post3 = Post.objects.create(
            id=3,
            city="Город 3",
            title="Город 3",
            image="https://link3.ru",
            text="Город 3",
        )
        self.post4 = Post.objects.create(
            id=4,
            city="Город 4",
            title="Город 4",
            image="https://link4.ru",
            text="Город 4",
        )
        self.post5 = Post.objects.create(
            id=5,
            city="Город 5",
            title="Город 5",
            image="https://link5.ru",
            text="Город 5",
        )
        self.post6 = Post.objects.create(
            id=6,
            city="Город 6",
            title="Город 6",
            image="https://link6.ru",
            text="Город 6",
        )
        self.post7 = Post.objects.create(
            id=7,
            city="Город 7",
            title="Город 7",
            image="https://link7.ru",
            text="Город 7",
        )
        self.post8 = Post.objects.create(
            id=8,
            city="Город 8",
            title="Город 8",
            image="https://link2.ru",
            text="Город 8",
        )
        self.post9 = Post.objects.create(
            id=9,
            city="Город 9",
            title="Город 9",
            image="https://link9.ru",
            text="Город 9",
        )
        self.post10 = Post.objects.create(
            id=10,
            city="Город 10",
            title="Город 10",
            image="https://link10.ru",
            text="Город 10",
        )

    def test_get(self):
        url = reverse("posts-list")

        response = self.client.get(url)
        serializer_data = PostSerializer(
            [
                self.post10,
                self.post9,
                self.post8,
                self.post7,
                self.post6,
                self.post5,
                self.post4,
                self.post3,
                self.post2,
                self.post1,
            ],
            many=True,
        ).data

        print(f"{serializer_data=}")
        print(f"{response.data=}")

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_by_id(self):
        url = reverse("posts-detail", args=[2])

        response = self.client.get(url)
        serializer_data = PostSerializer(self.post2).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    # def test_last(self):
    #     view = PostViewSet()
    #     url = view.reverse_action("last", args=[])
    #     print(f"{url=}")

    #     response = self.client.get(url)
    #     print(f"{response.data=}")
    #     serializer_data = PostSerializer(
    #         [
    #             self.post1,
    #             self.post2,
    #             self.post3,
    #             self.post4,
    #             self.post5,
    #             self.post6,
    #             self.post7,
    #             self.post8,
    #             self.post9,
    #         ],
    #         many=True,
    #     ).data
    #     print(f"{serializer_data=}")

    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     self.assertEqual(serializer_data, response.data)