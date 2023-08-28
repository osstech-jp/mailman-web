"""Test basic server startup."""
from django.test import TestCase
from django.contrib.auth.models import User


class SanityTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.su = User.objects.create_superuser(
            'aperson', 'myemail@example.com', 'password')
        self.user = User.objects.create_user(
            'bperson', 'bee@example.com', 'password')

    # def test_basic_postorius(self):
    #     response = self.client.get('/', follow=True)
    #     assert response.status_code == 200

    def _test_endpoints(self, endpoint, as_admin=False, as_user=False):
        if as_admin:
            self.client.force_login(self.su)
        elif as_user:
            self.client.force_login(self.user)

        response = self.client.get(endpoint, follow=True)
        assert response.status_code == 200
        self.client.logout()

    def test_basic_hyperkitty(self):
        self._test_endpoints('/archives')
        self._test_endpoints('/archives', as_user=True)

    def test_basic_django(self):
        self._test_endpoints('/admin')
