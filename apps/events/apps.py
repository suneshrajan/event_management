"""Module imports"""
from django.apps import AppConfig


class EventsConfig(AppConfig):
    """
    app config
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.events"
