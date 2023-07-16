from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class TestHome(SimpleTestCase):
    def test_status_code(self):
        url = reverse('Home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        url = reverse('Home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')


class TestAbout(SimpleTestCase):
    def test_status_code(self):
        url = reverse('About')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        url = reverse('About')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')