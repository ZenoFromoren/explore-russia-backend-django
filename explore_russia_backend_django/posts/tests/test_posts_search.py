from rest_framework.test import APITestCase
from django.urls import reverse
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import status


class PostsApiTestCase(APITestCase):
	def setUp(self):
		self.post1 = Post.objects.create(
			id=1,
			city="Иваново",
			title="Конструктивизм, убитый трамвай и красивые троллейбусы",
			image="https://link1.ru",
			text="Статья про Иваново",
		)
		self.post2 = Post.objects.create(
			id=2,
			city="Ташкент",
			title="Очень достойно, колоритно, но с пугающим вождением",
			image="https://link2.ru",
			text="Статья про Ташкент",
		)			
		self.post3 = Post.objects.create(
			id=3,
			city="Нижний Новогород",
			title="Кайфовый центр, впечатляющая Волга и всё ещё живой трамвай",
			image="https://link3.ru",
			text="Статья про Нижний Новогород",
		)

	def test_search_part(self):
		url = reverse("posts-list") + '?search=ив'

		response = self.client.get(url)
		serializer_data = PostSerializer(
			[self.post1, self.post3], many=True
		).data

		self.assertEqual(status.HTTP_200_OK, response.status_code)
		self.assertEqual(serializer_data, response.data)

	def test_search_all(self):
		url = reverse("posts-list") + '?search=и'

		response = self.client.get(url)
		serializer_data = PostSerializer(
			[self.post1, self.post2, self.post3], many=True
		).data

		self.assertEqual(status.HTTP_200_OK, response.status_code)
		self.assertEqual(serializer_data, response.data)

	def test_search_nothing(self):
		url = reverse("posts-list") + '?search=ывмывм'

		response = self.client.get(url)

		self.assertEqual(status.HTTP_200_OK, response.status_code)
		self.assertEqual([], response.data)
