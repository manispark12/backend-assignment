from django.test import TestCase
from rest_framework.test import APIClient
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        FAQ.objects.create(question="What is Django?", answer="A web framework.", language="en")
        FAQ.objects.create(question="क्या है Django?", answer="एक वेब फ्रेमवर्क।", language="hi")

    def test_faq_translation(self):
        client = APIClient()
        response = client.get('/api/faqs/', {'lang': 'hi'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['question'], "क्या है Django?")

    def test_faq_default_language(self):
        client = APIClient()
        response = client.get('/api/faqs/', {'lang': 'en'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['question'], "What is Django?")

    def test_cache_behavior(self):
        client = APIClient()
        # First request, should be a cache miss and fetch from the DB
        response_1 = client.get('/api/faqs/', {'lang': 'en'})
        # Second request, should be a cache hit
        response_2 = client.get('/api/faqs/', {'lang': 'en'})
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(response_1.data, response_2.data)  # Should be the same as it came from cache

# Create your tests here.
