"""Module imports"""
# pylint: disable=C0412, E0401, R0205, R0903, E1101, W0718
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from apps.events.models import EventCategory, Event, Ticket
from utils.swgr_doc_schmas import EventCategorySchema, EventSchema, EventTicketSchema
from apps.events.serializers import (
    EventCategorySerializer,
    EventSerializer,
    TicketSerializer,
    TicketDetailSerializer,
)


class EventCategoryView(APIView):
    """
    Event Category View -  List & Create event category
    """

    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        tags=EventCategorySchema.get_tag_common(),
        operation_id=EventCategorySchema.get_operation_id_list(),
        operation_summary=EventCategorySchema.get_opration_summary_list(),
        operation_description=EventCategorySchema.get_operation_description_list(),
        responses=EventCategorySchema.get_responses_list(),
    )
    def get(self, request):
        """
        List event category
        """

        try:
            category_obj = EventCategory.objects.all().order_by("-id")
            result = EventCategorySerializer(category_obj, many=True).data
            return Response(result, status=status.HTTP_200_OK)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @swagger_auto_schema(
        tags=EventCategorySchema.get_tag(),
        operation_id=EventCategorySchema.get_operation_id_create(),
        operation_summary=EventCategorySchema.get_opration_summary_create(),
        operation_description=EventCategorySchema.get_operation_description_create(),
        request_body=EventCategorySerializer,
        responses=EventCategorySchema.get_responses_create(),
    )
    def post(self, request):
        """
        Create event category
        """

        try:
            if not request.user.is_superuser:
                return Response(
                    {"detail": "You do not have permission to perform this action."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            serializer = EventCategorySerializer(data=request.data)
            if serializer.is_valid():
                # Create Event Category
                serializer.save()
                return Response(
                    {"detail": "Event category created successfuly."},
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class EventCategoryDetailView(APIView):
    """
    Event Category Detail View - Detail, Update, Delete event category
    """

    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        tags=EventCategorySchema.get_tag_common(),
        operation_id=EventCategorySchema.get_operation_id_detail(),
        operation_summary=EventCategorySchema.get_opration_summary_detail(),
        operation_description=EventCategorySchema.get_operation_description_detail(),
        responses=EventCategorySchema.get_responses_create(),
    )
    def get(self, request, _pk):
        """
        Event Category Detail
        """

        try:
            try:
                category = EventCategory.objects.get(pk=_pk)
            except EventCategory.DoesNotExist:
                return Response(
                    {"detail": "Event category not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            result = EventCategorySerializer(category).data
            return Response(result, status=status.HTTP_200_OK)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @swagger_auto_schema(
        tags=EventCategorySchema.get_tag(),
        operation_id=EventCategorySchema.get_operation_id_update(),
        operation_summary=EventCategorySchema.get_opration_summary_update(),
        operation_description=EventCategorySchema.get_operation_description_update(),
        request_body=EventCategorySerializer,
        responses=EventCategorySchema.get_responses_update(),
    )
    def put(self, request, _pk):
        """
        Update Event Category
        """

        try:
            if not request.user.is_superuser:
                return Response(
                    {"detail": "You do not have permission to perform this action."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            try:
                category = EventCategory.objects.get(pk=_pk)
            except EventCategory.DoesNotExist:
                return Response(
                    {"detail": "Event category not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = EventCategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"detail": "Event category updated successfuly."},
                    status=status.HTTP_200_OK,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @swagger_auto_schema(
        tags=EventCategorySchema.get_tag(),
        operation_id=EventCategorySchema.get_operation_id_delete(),
        operation_summary=EventCategorySchema.get_opration_summary_delete(),
        operation_description=EventCategorySchema.get_operation_description_delete(),
        responses=EventCategorySchema.get_responses_delete(),
    )
    def delete(self, request, _pk):
        """
        Delete Event Category
        """

        try:
            if not request.user.is_superuser:
                return Response(
                    {"detail": "You do not have permission to perform this action."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            try:
                category = EventCategory.objects.get(pk=_pk)
            except EventCategory.DoesNotExist:
                return Response(
                    {"detail": "Event category not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            category.delete()
            return Response(
                {"detail": "Event category deleted successfuly."},
                status=status.HTTP_200_OK,
            )
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class EventView(APIView):
    """
    Event View - List & Create event
    """

    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        tags=EventSchema.get_tag_common(),
        operation_id=EventSchema.get_operation_id_list(),
        operation_summary=EventSchema.get_opration_summary_list(),
        operation_description=EventSchema.get_operation_description_list(),
        responses=EventSchema.get_responses_list(),
    )
    def get(self, request):
        """
        List events
        """

        try:
            event_obj = Event.objects.all().order_by("-event_date")
            if not request.user.is_superuser:
                event_obj = event_obj.filter(
                    event_date__date__gte=timezone.now().date()
                ).order_by("-event_date")
            result = EventSerializer(event_obj, many=True).data
            return Response(result, status=status.HTTP_200_OK)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @swagger_auto_schema(
        tags=EventSchema.get_tag(),
        operation_id=EventSchema.get_operation_id_create(),
        operation_summary=EventSchema.get_opration_summary_create(),
        operation_description=EventSchema.get_operation_description_create(),
        request_body=EventSerializer,
        responses=EventSchema.get_responses_create(),
    )
    def post(self, request):
        """
        Create events
        """

        try:
            if not request.user.is_superuser:
                return Response(
                    {"detail": "You do not have permission to perform this action."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            serializer = EventSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"detail": "Event created successfuly."},
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class EventDetailView(APIView):
    """
    Event Detail View - Detail, Update & Delete event
    """

    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        tags=EventSchema.get_tag_common(),
        operation_id=EventSchema.get_operation_id_detail(),
        operation_summary=EventSchema.get_opration_summary_detail(),
        operation_description=EventSchema.get_operation_description_detail(),
        responses=EventSchema.get_responses_create(),
    )
    def get(self, request, _pk):
        """
        Event Detail
        """

        try:
            try:
                event_obj = Event.objects.get(pk=_pk)
            except Event.DoesNotExist:
                return Response(
                    {"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND
                )
            result = EventSerializer(event_obj).data
            return Response(result, status=status.HTTP_200_OK)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @swagger_auto_schema(
        tags=EventSchema.get_tag(),
        operation_id=EventSchema.get_operation_id_update(),
        operation_summary=EventSchema.get_opration_summary_update(),
        operation_description=EventSchema.get_operation_description_update(),
        request_body=EventSerializer,
        responses=EventSchema.get_responses_update(),
    )
    def put(self, request, _pk):
        """
        Update Event
        """

        try:
            if not request.user.is_superuser:
                return Response(
                    {"detail": "You do not have permission to perform this action."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            try:
                event_obj = Event.objects.get(pk=_pk)
            except Event.DoesNotExist:
                return Response(
                    {"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND
                )

            serializer = EventSerializer(event_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"detail": "Event updated successfuly."}, status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @swagger_auto_schema(
        tags=EventSchema.get_tag(),
        operation_id=EventSchema.get_operation_id_delete(),
        operation_summary=EventSchema.get_opration_summary_delete(),
        operation_description=EventSchema.get_operation_description_delete(),
        responses=EventSchema.get_responses_delete(),
    )
    def delete(self, request, _pk):
        """
        Delete Event
        """

        try:
            if not request.user.is_superuser:
                return Response(
                    {"detail": "You do not have permission to perform this action."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            try:
                event_obj = Event.objects.get(pk=_pk)
            except Event.DoesNotExist:
                return Response(
                    {"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND
                )

            event_obj.delete()
            return Response(
                {"detail": "Event deleted successfuly."}, status=status.HTTP_200_OK
            )
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class EventSearchView(APIView):
    """
    Event Search View - search event based on Category, Title, Description, Event Date
    """

    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description", "event_date", "category__name"]

    @swagger_auto_schema(
        tags=EventSchema.get_tag_common(),
        operation_id=EventSchema.get_operation_id_search(),
        operation_summary=EventSchema.get_opration_summary_search(),
        operation_description=EventSchema.get_operation_description_search(),
        manual_parameters=EventSchema.get_manual_parameters_search(),
        responses=EventSchema.get_responses_list(),
    )
    def get(self, request):
        """
        Search event
        """

        try:
            search_term = request.GET.get("search", "")
            queryset = Event.objects.all().order_by("-event_date")

            if not request.user.is_superuser:
                queryset = queryset.filter(
                    event_date__date__gte=timezone.now().date()
                ).order_by("-event_date")

            queryset = (
                queryset.filter(title__icontains=search_term)
                | queryset.filter(category__name__icontains=search_term)
                | queryset.filter(description__icontains=search_term)
                | queryset.filter(event_date__icontains=search_term)
            )

            result = EventSerializer(instance=queryset, many=True).data
            return Response(result, status=status.HTTP_200_OK)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class EventTicketView(APIView):
    """
    Event Ticket View - List & Book ticket
    """

    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        tags=EventTicketSchema.get_tag(),
        operation_id=EventTicketSchema.get_operation_id_list(),
        operation_summary=EventTicketSchema.get_opration_summary_list(),
        operation_description=EventTicketSchema.get_operation_description_list(),
        responses=EventTicketSchema.get_responses_list(),
    )
    def get(self, request):
        """
        List booked ticket
        """

        try:
            ticket_obj = Ticket.objects.filter(user_id=request.user.id).order_by(
                "-event__event_date"
            )
            result = TicketDetailSerializer(ticket_obj, many=True).data
            return Response(result, status=status.HTTP_200_OK)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @swagger_auto_schema(
        tags=EventTicketSchema.get_tag(),
        operation_id=EventTicketSchema.get_operation_id_create(),
        operation_summary=EventTicketSchema.get_opration_summary_create(),
        operation_description=EventTicketSchema.get_operation_description_create(),
        request_body=TicketSerializer,
        responses=EventTicketSchema.get_responses_create(),
    )
    def post(self, request):
        """
        Book ticket
        """

        try:
            if request.user.id != int(request.data['user']):
                return Response(
                    {"detail": "You do not have permission to perform this action."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            serializer = TicketSerializer(data=request.data)
            if serializer.is_valid():
                # Create Event Category
                serializer.save()
                return Response(
                    {"detail": "Tickets booked successfuly."},
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class EventTicketDetailView(APIView):
    """
    Event Ticket Detail View - Ticket Details
    """

    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        tags=EventTicketSchema.get_tag(),
        operation_id=EventTicketSchema.get_operation_id_detail(),
        operation_summary=EventTicketSchema.get_opration_summary_detail(),
        operation_description=EventTicketSchema.get_operation_description_detail(),
        responses=EventTicketSchema.get_responses_detail(),
    )
    def get(self, request, _pk):
        """
        Ticket detail
        """

        try:
            try:
                ticket_obj = Ticket.objects.get(pk=_pk)
            except Ticket.DoesNotExist:
                return Response(
                    {"detail": "Ticket not found."}, status=status.HTTP_404_NOT_FOUND
                )
            result = TicketDetailSerializer(ticket_obj).data
            return Response(result, status=status.HTTP_200_OK)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
