"""Module imports"""
# pylint: disable=E0401
from django.urls import path
from apps.events import views

urlpatterns = [
    path(
        "categories/", 
        views.EventCategoryView.as_view(),
        name="category-list"
    ),
    path(
        "categories/<int:_pk>/",
        views.EventCategoryDetailView.as_view(),
        name="category-details",
    ),
    path(
        "events/", 
        views.EventView.as_view(),
        name="event-list"
    ),
    path(
        "events/<int:_pk>/", 
        views.EventDetailView.as_view(),
        name="event-details"
    ),
    path(
        "search/events/", 
        views.EventSearchView.as_view(),
        name="search-event"
    ),
    path(
        "tickets/", 
        views.EventTicketView.as_view(),
        name="ticket-list"
    ),
    path(
        "tickets/<int:_pk>/",
        views.EventTicketDetailView.as_view(),
        name="ticket-details",
    ),
]
