from django.urls import reverse, resolve
from django.test import TestCase
from website.views import home, about, pricing, service, contact, appointment

class TestUrls(TestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_about_url(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_service_url(self):
        url = reverse('service')
        self.assertEqual(resolve(url).func, service)

    def test_pricing_url(self):
        url = reverse('pricing')
        self.assertEqual(resolve(url).func, pricing)


    def test_contact_url(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)

    def test_appointment_url(self):
        url = reverse('appointment')
        self.assertEqual(resolve(url).func, appointment)