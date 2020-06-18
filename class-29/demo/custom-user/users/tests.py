from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import CustomUser

class TestCustomUser(TestCase):

    def test_creation(self):
        user = get_user_model().objects.create_user(
            username='tester',
            email='tester@email.com',
            password='pass'
        )

        self.assertIsInstance(user, CustomUser)
        self.assertEqual(user.email, 'tester@email.com')
        self.assertIsNotNone(user.password)

    def test_no_dupe_email(self):
        user_1 = get_user_model().objects.create_user(
            username='tester',
            email='tester@email.com',
            password='pass'
        )

        try:
            user_2 = get_user_model().objects.create_user(
                username='nottester',
                email='tester@email.com',
                password='pass'
            )
        except IntegrityError:

            print('all good')

        else:
            self.fail('no bueno')
