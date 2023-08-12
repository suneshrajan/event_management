"""Module imports"""
# pylint: disable=E0401, E1101, R0205, R0903, W0237
from rest_framework import serializers
from django.utils import timezone
from .models import Event, Ticket, EventCategory


class EventCategorySerializer(serializers.ModelSerializer):
    """
    Event Category Serializer
    """

    class Meta:
        """
        Inner Meta class
        """

        model = EventCategory
        fields = ["id", "name", "code"]


class EventSerializer(serializers.ModelSerializer):
    """
    Event Serializer
    """

    class Meta:
        """
        Inner Meta class
        """

        model = Event
        fields = [
            "id",
            "title",
            "description",
            "category",
            "max_seats",
            "booking_start",
            "booking_end",
            "event_date",
        ]

    def validate(self, data):
        if data["booking_end"] < data["booking_start"]:
            raise serializers.ValidationError(
                "Booking end must be greater than or equal to booking start."
            )

        if data["booking_end"] < timezone.now():
            raise serializers.ValidationError(
                "Booking end must be greater than current date."
            )

        if data["event_date"] < data["booking_end"]:
            raise serializers.ValidationError(
                "Event date must be greater than or equal to booking end."
            )

        return data


class TicketSerializer(serializers.ModelSerializer):
    """
    Ticket Serializer
    """

    class Meta:
        """
        Inner Meta class
        """

        model = Ticket
        fields = ["user", "event", "ticket_count", "booked_at"]

    def validate(self, data):
        if data["event"].booking_end <= timezone.now():
            raise serializers.ValidationError(
                "Sorry!, You can't book the tickets. Booking time is already over."
            )

        if data["event"].max_seats < data["ticket_count"]:
            raise serializers.ValidationError(
                f"Sorry!, Only {data['event'].max_seats} avaliable."
            )

        if data["event"].max_seats == 0:
            raise serializers.ValidationError("Sorry!, House full.")

        if (
            data["event"].max_seats != 0
            and data["event"].max_seats > data["ticket_count"]
        ):
            event_obj = Event.objects.get(id=data["event"].id)
            event_obj.max_seats -= data["ticket_count"]
            event_obj.save()

        return data


class TicketDetailSerializer(serializers.ModelSerializer):
    """
    Ticket Detail Serializer
    """

    user_name = serializers.SerializerMethodField("get_user_name")

    title = serializers.SerializerMethodField("get_title")

    description = serializers.SerializerMethodField("get_description")

    category = serializers.SerializerMethodField("get_category")

    event_date = serializers.SerializerMethodField("get_event_date")

    ticket_id = serializers.SerializerMethodField("get_ticket_id")

    def get_user_name(self, obj):
        """
        Get user name form User table
        """

        return obj.user.first_name + "" + obj.user.last_name

    def get_title(self, obj):
        """
        Get event title form Event table
        """

        return obj.event.title

    def get_description(self, obj):
        """
        Get event description form Event table
        """

        return obj.event.description

    def get_category(self, obj):
        """
        Get category name form EventCategory table
        """

        return obj.event.category.name

    def get_event_date(self, obj):
        """
        Get event date form Event table
        """

        return obj.event.event_date

    def get_ticket_id(self, obj):
        """
        Get ticket id form Ticket table
        """
        return obj.id

    class Meta:
        """
        Inner Meta class
        """

        model = Ticket
        fields = [
            "user",
            "user_name",
            "event",
            "title",
            "description",
            "category",
            "event_date",
            "ticket_id",
            "ticket_count",
            "booked_at",
        ]
