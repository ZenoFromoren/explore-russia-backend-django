from django.test import TestCase
from posts.models import Post
from posts.serializers import PostSerializer


class PostSerializerTestCase(TestCase):
    def test_correct(self):
        post1 = Post.objects.create(
            city="Город 1", title="Город 1", image="https://link1.ru", text="Город 1"
        )
        post2 = Post.objects.create(
            city="Город 2", title="Город 2", image="https://link2.ru", text="Город 2"
        )
        post3 = Post.objects.create(
            city="Город 3", title="Город 3", image="https://link3.ru", text="Город 3"
        )

        data = PostSerializer([post1, post2, post3], many=True).data
        # print(data)
        expected_data = [
            {
                "id": post1.id,
                "city": "Город 1",
                "title": "Город 1",
                "image": "https://link1.ru",
                "text": "Город 1",
                "created_at": post1.created_at.isoformat(),
                "updated_at": post1.updated_at.isoformat(),
            },
            {
                "id": post2.id,
                "city": "Город 2",
                "title": "Город 2",
                "image": "https://link2.ru",
                "text": "Город 2",
                "created_at": post2.created_at.isoformat(),
                "updated_at": post2.updated_at.isoformat(),
            },
            {
                "id": post3.id,
                "city": "Город 3",
                "title": "Город 3",
                "image": "https://link3.ru",
                "text": "Город 3",
                "created_at": post3.created_at.isoformat(),
                "updated_at": post3.updated_at.isoformat(),
            },
        ]
        # print(expected_data)

        # self.assertEqual(expected_data, data)
