from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User
from django.conf import settings

class SimpleAuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a user for login/authentication tests
        self.user = User.objects.create_user(
            name='Test User',
            email='testuser@example.com',
            password='testpass',
            role='wholesaler',
            phone_number='0700111222'
        )
        # Create an admin user (add to whitelist if needed)
        self.admin = User.objects.create_user(
            name='Admin User',
            email='admin@example.com',
            password='adminpass',
            role='admin',
            phone_number='0700333444'
        )
        settings.ADMIN_EMAIL_WHITELIST = ['admin@example.com']

    def test_register(self):
        response = self.client.post(reverse('register'), {
            'name': 'New User',
            'email': 'newuser@example.com',
            'password': 'newpass',
            'role': 'wholesaler',
            'phone_number': '0712345678'
            # 'location' is not required for wholesalers
        })
        print("Register response:", response.data)  # Debug output
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_200_OK])

    def test_login_wholesaler(self):
        response = self.client.post(reverse('login'), {
            'email': 'testuser@example.com',
            'password': 'testpass'
        })
        print("Wholesaler login response:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_admin_whitelisted(self):
        response = self.client.post(reverse('login'), {
            'email': 'admin@example.com',
            'password': 'adminpass'
        })
        print("Whitelisted admin login response:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_admin_not_whitelisted(self):
        # Remove admin from whitelist
        settings.ADMIN_EMAIL_WHITELIST = []
        response = self.client.post(reverse('login'), {
            'email': 'admin@example.com',
            'password': 'adminpass'
        })
        print("Not whitelisted admin login response:", response.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn('error', response.data)

    def test_authenthication_view(self):
        # Log in first to get the token
        login_response = self.client.post(reverse('login'), {
            'email': 'testuser@example.com',
            'password': 'testpass'
        })
        token = login_response.data.get('token')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get(reverse('authenthication'))
        print("Authentication view response:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)