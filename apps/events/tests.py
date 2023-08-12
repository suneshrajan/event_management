"""Module imports"""
# pylint: disable=C0412, E0401, R0205, R0903, E1101
from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.utils import timezone
from apps.accounts.models import User
from apps.events.models import EventCategory, Event, Ticket


class EventCategoryViewTestCase(TestCase):
    """
    Event Category View TestCase
    """

    def setUp(self):
        """
        settingup everything
        """

        self.client = APIClient()
        self.category_url = reverse("category-list")
        self.user = User.objects.create_user(
            email="admin@example.com", password="adminpassword", is_superuser=True
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_get_event_categories(self):
        """
        Test get event categories
        """

        category = EventCategory.objects.create(name="Music", code="MUSIC")

        response = self.client.get(self.category_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], category.name)

    def test_create_event_category(self):
        """
        Test create event categories
        """

        data = {"name": "Sports", "code": "SPORTS"}

        response = self.client.post(self.category_url, data, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EventCategory.objects.count(), 1)
        self.assertEqual(EventCategory.objects.get().name, "Sports")

    def test_create_event_category_without_credentials(self):
        """
        Test create event category without credentials
        """

        self.client.credentials()  # Remove authentication

        data = {"name": "Sports", "code": "SPORTS"}

        response = self.client.post(self.category_url, data, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(EventCategory.objects.count(), 0)


class EventCategoryDetailViewTestCase(TestCase):
    """
    Event Category Detail View TestCase
    """

    def setUp(self):
        """
        settingup everything
        """

        self.client = APIClient()
        self.category_url = reverse("category-list")
        self.user = User.objects.create_user(
            email="admin@example.com", password="adminpassword", is_superuser=True
        )
        self.token = Token.objects.create(user=self.user)
        self.category = EventCategory.objects.create(name="Music", code="MUSIC")
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_get_event_category_detail(self):
        """
        Test get event category detail
        """

        response = self.client.get(f"{self.category_url}{self.category.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.category.name)

    def test_update_event_category(self):
        """
        Test update event category detail
        """

        data = {"name": "Sports", "code": "SPORTS"}

        response = self.client.put(
            f"{self.category_url}{self.category.id}/", data, format="multipart"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(EventCategory.objects.get(id=self.category.id).name, "Sports")

    def test_delete_event_category(self):
        """
        Test delete event category
        """

        response = self.client.delete(f"{self.category_url}{self.category.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(EventCategory.objects.filter(id=self.category.id).exists())


class EventViewTestCase(TestCase):
    """
    Event View TestCase
    """

    def setUp(self):
        """
        Settingup everything
        """

        self.client = APIClient()
        self.event_url = reverse("event-list")
        self.user = User.objects.create_user(
            email="admin@example.com", password="adminpassword", is_superuser=True
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_get_event_list_as_admin(self):
        """
        Test get event list as admin
        """

        response = self.client.get(self.event_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_event_list_as_user(self):
        """
        Test get event list as user
        """

        user = User.objects.create_user(
            email="user@example.com", password="userpassword"
        )
        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

        response = client.get(self.event_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_event_as_admin(self):
        """
        Test create event list as admin
        """

        category = EventCategory.objects.create(name="Music", code="MUSIC")
        data = {
            "title": "Music Concert",
            "description": "Enjoy live music!",
            "category": category.id,
            "max_seats": 100,
            "booking_start": timezone.now() - timedelta(days=3),
            "booking_end": timezone.now() + timedelta(days=1),
            "event_date": timezone.now() + timedelta(days=3),
        }

        response = self.client.post(self.event_url, data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_event_as_admin_with_wrong_data(self):
        """
        Test get event list as admin with wrong data
        """

        category = EventCategory.objects.create(name="Music", code="MUSIC")
        data = {
            "title": "Music Concert",
            "description": "Enjoy live music!",
            "category": category,
            "max_seats": 100,
            "booking_start": timezone.now(),
            "booking_end": timezone.now(),
            "event_date": timezone.now(),
        }

        response = self.client.post(self.event_url, data, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class EventDetailViewTestCase(TestCase):
    """
    Event Detail View TestCase
    """

    def setUp(self):
        """
        Settingup Everything
        """

        self.client = APIClient()
        self.event_url = reverse("event-list")
        self.user = User.objects.create_user(
            email="admin@example.com", password="adminpassword", is_superuser=True
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_get_event_detail(self):
        """
        Test get event detail
        """

        category = EventCategory.objects.create(name="Music", code="MUSIC")
        event = Event.objects.create(
            title="Music Concert",
            description="Enjoy live music!",
            category=category,
            max_seats=100,
            booking_start=timezone.now() - timedelta(days=3),
            booking_end=timezone.now() - timedelta(days=1),
            event_date=timezone.now() + timedelta(days=1),
        )

        response = self.client.get(f"{self.event_url}{event.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_event(self):
        """
        Test update event detail
        """

        category = EventCategory.objects.create(name="Music", code="MUSIC")
        event = Event.objects.create(
            title="Music Concert",
            description="Enjoy live music!",
            category=category,
            max_seats=100,
            booking_start=timezone.now() - timedelta(days=3),
            booking_end=timezone.now() - timedelta(days=1),
            event_date=timezone.now() + timedelta(days=1),
        )

        data = {
            "title": "Updated Concert",
            "description": "Updated description",
            "category": category.id,
            "max_seats": 200,
            "booking_start": timezone.now() - timedelta(days=3),
            "booking_end": timezone.now() + timedelta(days=1),
            "event_date": timezone.now() + timedelta(days=3),
        }

        response = self.client.put(
            f"{self.event_url}{event.id}/", data, format="multipart"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_event(self):
        """
        Test delete event
        """

        category = EventCategory.objects.create(name="Music", code="MUSIC")
        event = Event.objects.create(
            title="Music Concert",
            description="Enjoy live music!",
            category=category,
            max_seats=100,
            booking_start=timezone.now() - timedelta(days=3),
            booking_end=timezone.now() - timedelta(days=1),
            event_date=timezone.now() + timedelta(days=1),
        )

        response = self.client.delete(f"{self.event_url}{event.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EventSearchViewTestCase(TestCase):
    """
    Event Search View TestCase
    """

    def setUp(self):
        """
        Settingup everything
        """

        self.client = APIClient()
        self.event_search_url = reverse("search-event")
        self.user = User.objects.create_user(
            email="admin@example.com", password="adminpassword", is_superuser=True
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_search_events(self):
        """
        Test search events API
        """

        category = EventCategory.objects.create(name="Music Event", code="MUSIC")
        category2 = EventCategory.objects.create(name="Comedy Event", code="COMEDY")

        Event.objects.create(
            title="Music Concert",
            description="Enjoy live music!",
            category=category,
            max_seats=100,
            booking_start=timezone.now() - timedelta(days=3),
            booking_end=timezone.now() - timedelta(days=1),
            event_date=timezone.now() + timedelta(days=1),
        )

        Event.objects.create(
            title="Comedy Show",
            description="Laugh your heart out!",
            category=category2,
            max_seats=50,
            booking_start=timezone.now() - timedelta(days=3),
            booking_end=timezone.now(),
            event_date=timezone.now() + timedelta(days=2),
        )

        response = self.client.get(self.event_search_url, {"search": "Music Concert"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.event_search_url, {"search": "Comedy"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.event_search_url, {"search": "Event"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class EventTicketViewTestCase(TestCase):
    """
    Event Ticket View TestCase
    """

    def setUp(self):
        """
        Settingup everything
        """

        self.client = APIClient()
        self.ticket_url = reverse("ticket-list")
        self.user = User.objects.create_user(
            email="user@example.com", password="userpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.category = EventCategory.objects.create(name="Music Event", code="MUSIC")

        self.event = Event.objects.create(
            title="Music Concert",
            description="Enjoy live music!",
            category=self.category,
            max_seats=100,
            booking_start=timezone.now() - timedelta(days=3),
            booking_end=timezone.now() + timedelta(days=1),
            event_date=timezone.now() + timedelta(days=2),
        )

    def test_list_tickets(self):
        """
        Test list all booked tickets
        """

        Ticket.objects.create(user=self.user, event=self.event, ticket_count=2)

        response = self.client.get(self.ticket_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_ticket(self):
        """
        Test book ticket
        """

        ticket_data = {
            "user": self.user.id,
            "event": self.event.id,
            "ticket_count": 2,
        }

        response = self.client.post(self.ticket_url, ticket_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["detail"], "Tickets booked successfuly.")

    def test_create_ticket_invalid_event(self):
        """
        Test book ticket for an invalid event
        """

        # Trying to book tickets for an invalid event
        ticket_data = {
            "user": self.user.id,
            "event": 999,  # Invalid event ID
            "ticket_count": 2,
        }

        response = self.client.post(self.ticket_url, ticket_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_ticket_invalid_quantity(self):
        """
        Test book ticket for an invalid quantity
        """

        # Trying to book tickets with an invalid quantity
        ticket_data = {
            "user": self.user.id,
            "event": self.event.id,
            "ticket_count": -1,  # Invalid quantity
        }

        response = self.client.post(self.ticket_url, ticket_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class EventTicketDetailViewTestCase(TestCase):
    """
    Event Ticket Detail View TestCase
    """

    def setUp(self):
        """
        Settingup everything
        """

        self.client = APIClient()
        self.ticket_url = reverse("ticket-list")
        self.user = User.objects.create_user(
            email="user@example.com", password="userpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        self.category = EventCategory.objects.create(name="Music Event", code="MUSIC")

        self.event = Event.objects.create(
            title="Music Concert",
            description="Enjoy live music!",
            category=self.category,
            max_seats=100,
            booking_start=timezone.now(),
            booking_end=timezone.now(),
            event_date=timezone.now(),
        )

        self.ticket = Ticket.objects.create(
            user=self.user, event=self.event, ticket_count=2
        )

    def test_get_ticket(self):
        """
        Test get ticket details
        """

        response = self.client.get(f"{self.ticket_url}{self.ticket.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["event"], self.event.id)

    def test_get_invalid_ticket(self):
        """
        Test get invalid ticket details
        """

        # Trying to get a ticket with an invalid ID
        response = self.client.get(f"{self.ticket_url}999/")  # Invalid ticket ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
