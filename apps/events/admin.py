"""Module imports"""
# pylint: disable=W0611
from django.contrib import admin
from apps.events.models import EventCategory, Event, Ticket


# Register Needed Models
admin.site.register(EventCategory)
admin.site.register(Event)
admin.site.register(Ticket)