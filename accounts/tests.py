from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class SignUPViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='test1',
            email='test@test.com'
        )

    def test_setup_view_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_form(self):
        response = self.client.post(reverse('signup'),
                                    {'username': self.user.username, 'first_name': 'test1', 'last_name': 'test1last',
                                     'email': self.user.email, ' age': 19})
        self.assertEqual(get_user_model().objects.all()[0].username, self.user.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.user.email)
