from django.test import TestCase, Client
from django.urls import reverse

class TestIndexViews(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index_shop'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content.decode('UTF-8'), 'Index of mylists')

    def test_index_tpl_view(self):
        response = self.client.get(reverse('index_shop_render'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content.decode('UTF-8'), '<h1>Index Shopping lists</h1>')

    def test_index_tpl_used(self):
        response = self.client.get(reverse('index_shop_render'))
        self.assertTemplateUsed(response, 'index.html')

    @classmethod
    def tearDownClass(cls):
        cls.client = None