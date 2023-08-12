"""Module imports"""
# pylint: disable=E0401, R0205, R0903, E1101
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from apps.accounts.models import User


class UserSignupTestCase(TestCase):
    """
    User Sighup TestCase
    """

    def setUp(self):
        """
        Setup everything
        """
        self.client = APIClient()
        self.signup_url = reverse("user-signup")

    def test_user_signup(self):
        """
        Test user signup
        """
        data = {
            "email": "test@example.com",
            "password": "testpassword",
            "first_name": "John",
            "last_name": "Doe",
        }

        response = self.client.post(self.signup_url, data, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Token.objects.count(), 1)
        self.assertEqual(response.data["detail"], "User created successfully.")

    def test_user_signup_invalid_data(self):
        """
        Test user signup with invalid data
        """

        data = {
            "email": "invalidemail",
            "password": "testpassword",
            "first_name": "John",
            "last_name": "Doe",
        }

        response = self.client.post(self.signup_url, data, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(Token.objects.count(), 0)

    def test_user_signup_duplicate_email(self):
        """
        Test user signup with duplicate email
        """

        # Create a user with the same email
        User.objects.create_user(email="test@example.com", password="password")

        payload = {
            "email": "test@example.com",
            "password": "testpassword",
            "first_name": "John",
            "last_name": "Doe",
        }

        response = self.client.post(self.signup_url, payload, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Token.objects.count(), 0)


class UserLoginTestCase(TestCase):
    """
    User Login TestCase
    """

    def setUp(self):
        """
        Setup everything
        """

        self.client = APIClient()
        self.login_url = reverse("user-login")
        self.user = User.objects.create_user(
            email="test@example.com", password="testpassword"
        )

    def test_user_login(self):
        """
        Test user login
        """

        data = {
            "email": "test@example.com",
            "password": "testpassword",
        }

        response = self.client.post(self.login_url, data, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("token" in response.data)
        self.assertTrue("data" in response.data)
        self.assertEqual(response.data["detail"], "User login successful")

    def test_user_login_invalid_credentials(self):
        """
        Test user login invalid credentials
        """

        data = {
            "email": "test@example.com",
            "password": "wrongpassword",
        }

        response = self.client.post(self.login_url, data, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse("token" in response.data)
        self.assertFalse("data" in response.data)
        self.assertEqual(response.data["detail"], "User password wrong.")

    def test_user_login_user_not_found(self):
        """
        Test user login user not found check
        """

        data = {
            "email": "nonexistent@example.com",
            "password": "testpassword",
        }

        response = self.client.post(self.login_url, data, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse("token" in response.data)
        self.assertFalse("data" in response.data)
        self.assertEqual(response.data["detail"], "User not found.")


class UserLogoutTestCase(TestCase):
    """
    User Logout TestCase
    """

    def setUp(self):
        """
        Setup everything
        """

        self.client = APIClient()
        self.logout_url = reverse("user-logout")
        self.user = User.objects.create_user(
            email="test@example.com", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)

    def test_user_logout(self):
        """
        Test user logout
        """

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        response = self.client.get(self.logout_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Token.objects.filter(user=self.user).exists())

    def test_user_logout_unauthenticated(self):
        """
        Test user logout unauthenticated
        """

        response = self.client.get(self.logout_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(Token.objects.filter(user=self.user).exists())
