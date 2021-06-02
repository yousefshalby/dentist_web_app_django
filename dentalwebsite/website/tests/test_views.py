from django.test import TestCase
from django.urls import reverse, resolve


class TestViews (TestCase):
    
    def setUp(self):
        self.home_url = reverse('home')
        self.about_url = reverse('about')
        self.pricing_url = reverse('pricing')
        self.service_url = reverse('service')
        self.contact_url = reverse('contact')
        self.appointment_url = reverse('appointment')


    def test_home_view(self):
        response= self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')


    def test_about_view(self):
        response= self.client.get(self.about_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')


    def test_service_view(self):
        response= self.client.get(self.service_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service.html')

    def test_pricing_view(self):
        response= self.client.get(self.pricing_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pricing.html')

    def test_contact_view(self):
        response= self.client.get(self.contact_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html') 

    def test_appointment_view(self):
        response= self.client.get(self.appointment_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')                
