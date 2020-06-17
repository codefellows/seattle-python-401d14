from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='tester@email.com',
            password='pass'
        )

        self.snack = Snack.objects.create(
            name='pickle',
            description='refreshing',
            purchaser=self.user,
        )

    def test_string_representation(self):
        snack = Snack(name='Snicker')
        self.assertEqual(str(snack), snack.name)

    def test_snack_content(self):
        self.assertEqual(f'{self.snack.name}', 'pickle')
        self.assertEqual(f'{self.snack.purchaser}', 'tester')
        self.assertEqual(f'{self.snack.description}', 'refreshing')

    def test_snack_list_view(self):
        response = self.client.get(reverse('snack_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'pickle')
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_snack_detail_view(self):
        response = self.client.get('/snacks/1/')
        no_response = self.client.get('/snacks/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'refreshing')
        self.assertTemplateUsed(response, 'snack_detail.html')


    def test_snack_create_view(self):
        response = self.client.post(reverse('snack_create'), {
            'name': 'Chicharrones',
            'description': 'Low carb',
            'purchaser': self.user,
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chicharrones')
        self.assertContains(response, 'Low carb')


    def test_snack_update_view(self):
        response = self.client.post(reverse('snack_update',args='1'), {
            'name': 'Updated name',
            'description': 'Updated description',
        })
        self.assertEqual(response.status_code, 302)

    def test_snack_delete_view(self):
        response = self.client.get(reverse('snack_delete',args='1'))
        self.assertEqual(response.status_code, 200)
