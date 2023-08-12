"""Module imports"""
# pylint: disable=E0211, E0401, R0205, R0903, E1101
from drf_yasg import openapi


# Accounts
class SignupSchema:
    """
    Swagger attributes for Signup
    """

    def get_tag():
        """
        Headline Tag
        """

        tag = ["Accounts (User)"]
        return tag

    def get_operation_id():
        """
        Opration Unique ID
        """

        operation_id = "Signup - Create User"
        return operation_id

    def get_opration_summary():
        """
        Opration sort summary
        """

        opration_summary = """Signup Users"""
        return opration_summary

    def get_operation_description():
        """
        Opration description
        """

        desc = """
            Signup API
            -----------
            
            This API endpoint allows users to sign up by providing their email and password.

            **Endpoint:** POST api/accounts/signup/

            **Request Body:**

            - { "**email**": "string", "**password**": "string", "**first_name**": "string", "**last_name**": "string"}

            - **email (required):** The email address of the new user. It should be a valid email format.

            - **password (required):** The password for the new user. It should be kept secure and confidential.

            **Response:**
            
            - The API responds with a JSON array containing the following post details:

            - **id:** The unique identifier of the user.

            - **email:** The email id of the user.

            - **first_name:** First name of the user.

            - **last_name:** Last name of the user.

            **Note:**

            - This API is used to create a new user account.

            - Ensure that the provided email is unique.

            - The password should be kept secure and should meet any password complexity requirements.

        """
        return desc

    def get_manual_parameters():
        """
        Manual input parameters for swagger ui
        """

        manual_parameters = [
            openapi.Parameter(
                "first_name",
                openapi.IN_FORM,
                description="First Name",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "last_name",
                openapi.IN_FORM,
                description="Last Name",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "email",
                openapi.IN_FORM,
                description="Email",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_EMAIL,
                required=True,
            ),
            openapi.Parameter(
                "password",
                openapi.IN_FORM,
                description="Password",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_PASSWORD,
                required=True,
            ),
        ]
        return manual_parameters

    def get_consumes():
        """
        Type Consumes
        """

        consumes = ["multipart/form-data"]
        return consumes

    def get_responses():
        """
        Response of the api
        """

        responses = {
            201: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "token": openapi.Schema(type=openapi.TYPE_STRING),
                        "data": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                "username": openapi.Schema(type=openapi.TYPE_STRING),
                                "email": openapi.Schema(type=openapi.TYPE_STRING),
                                "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                                "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                            },
                        ),
                        "detail": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            500: "Internal Server Error",
        }
        return responses


class LoginSchema:
    """
    Swagger attributes for Login
    """

    def get_tag():
        """
        Headline Tag
        """

        tag = ["Accounts (User)"]
        return tag

    def get_operation_id():
        """
        Opration Unique ID
        """

        operation_id = "Signin - Login User"
        return operation_id

    def get_opration_summary():
        """
        Opration sort summary
        """

        opration_summary = """Signin Users"""
        return opration_summary

    def get_operation_description():
        """
        Opration description
        """

        desc_val = """
            Login API
            -----------

            This API endpoint allows users to authenticate by providing their username and password.

            **Endpoint:** POST api/accounts/login/

            **Request Body:**

            - { "**email**": "string", "**password**": "string" }

            - **email (required):** The email of the user for authentication.

            - **password (required):** The password associated with the provided username.

            **Response:**
            
            - The API responds with a JSON array containing the following post details:

            - **id:** The unique identifier of the user.

            - **email:** The unique email id of the user.

            - **first_name:** First name of the user.

            - **last_name:** Last name of the user.

            **Note:**

            - This API is used for user authentication and generating access tokens.

            - The provided username and password must be valid and associated with an existing user account.

            - The response may include an authentication token or session information for subsequent API calls.
        """
        return desc_val

    def get_manual_parameters():
        """
        Manual input parameters for swagger ui
        """

        manual_parameters = [
            openapi.Parameter(
                "email",
                openapi.IN_FORM,
                description="Email",
                type=openapi.TYPE_STRING,
                required=True,
            ),
            openapi.Parameter(
                "password",
                openapi.IN_FORM,
                description="Password",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_PASSWORD,
                required=True,
            ),
        ]
        return manual_parameters

    def get_responses():
        """
        Response of the api
        """

        responses = {
            200: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "token": openapi.Schema(type=openapi.TYPE_STRING),
                        "data": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                "email": openapi.Schema(type=openapi.TYPE_STRING),
                                "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                                "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                            },
                        ),
                        "detail": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            404: "Not Found",
            500: "Internal Server Error",
        }
        return responses


class LogOutSchema:
    """
    Swagger attributes for Logout
    """

    def get_tag():
        """
        Headline Tag
        """

        tag = ["Accounts (User)"]
        return tag

    def get_operation_id():
        """
        Opration Unique ID
        """

        operation_id = "Signout - Logout User"
        return operation_id

    def get_opration_summary():
        """
        Opration sort summary
        """

        opration_summary = "Signout Users"
        return opration_summary

    def get_operation_description():
        """
        Opration description
        """

        desc_val = """
            Logout API
            ----------

            Logout the authenticated user, and delete the user credentials.

            **Endpoint:** GET api/accounts/logout/

            **Authentication:**

            - This API requires authentication. Users must include a valid authentication token in the request headers for successful access.

        """
        return desc_val

    def get_responses():
        """
        Response of the api
        """

        responses = {200: "Successful logout", 500: "Internal Server Error"}
        return responses


# Events
class EventCategorySchema:
    """
    Swagger attributes for Event Category
    """

    def get_tag():
        """
        Headline Tag
        """

        tag = ["Event Category (Admin)"]
        return tag

    def get_tag_common():
        """
        Headline Tag
        """

        tag = ["Events (Admin & User)"]
        return tag

    def get_operation_id_list():
        """
        Opration Unique ID
        """

        operation_id = "Event Category List"
        return operation_id

    def get_operation_id_detail():
        """
        Opration Unique ID
        """

        operation_id = "Event Category Details"
        return operation_id

    def get_operation_id_create():
        """
        Opration Unique ID
        """

        operation_id = "Admin - Create Event Category"
        return operation_id

    def get_operation_id_update():
        """
        Opration Unique ID
        """

        operation_id = "Admin - Update Event Category"
        return operation_id

    def get_operation_id_delete():
        """
        Opration Unique ID
        """

        operation_id = "Admin - Delete Event Category"
        return operation_id

    def get_opration_summary_list():
        """
        Opration sort summary
        """

        opration_summary = """Event Category List"""
        return opration_summary

    def get_opration_summary_detail():
        """
        Opration sort summary
        """

        opration_summary = """Event Category Details"""
        return opration_summary

    def get_opration_summary_create():
        """
        Opration sort summary
        """

        opration_summary = """Create Event Category"""
        return opration_summary

    def get_opration_summary_update():
        """
        Opration sort summary
        """

        opration_summary = """Update Event Category"""
        return opration_summary

    def get_opration_summary_delete():
        """
        Opration sort summary
        """

        opration_summary = """Delete Event Category"""
        return opration_summary

    def get_operation_description_list():
        """
        Opration description
        """

        desc_val = """
            List Event Category API
            -----------

            This API endpoint allows to list Event Category.

            **Endpoint:** GET event/categories/

            **Response:**
            
            - The API responds with a JSON array containing the following post details:

            - **id:** The unique identifier of the Event Category.

            - **name:** The unique name of the Event Category.

            - **code:** The unique code of the Event Category.
        """
        return desc_val

    def get_operation_description_detail():
        """
        Opration description
        """

        desc_val = """
            Detail Event Category API
            -----------

            This API endpoint allows to check detail of the Event Category.

            **Endpoint:** GET event/categories/{cat_id}

            **URL Path Parameters:**
            
            - category_id (required): The unique identifier of the category.

            **Response:**
            
            - The API responds with a JSON array containing the following post details:

            - **id:** The unique identifier of the Event Category.

            - **name:** The unique name of the Event Category.

            - **code:** The unique code of the Event Category.

        """
        return desc_val

    def get_operation_description_create():
        """
        Opration description
        """

        desc_val = """
            Create Event Category API
            -----------

            This API endpoint allows admin to Create Event Category.

            **Endpoint:** POST event/categories/

            **Request Body:**

            - { "**name**": "string", "**code**": "string" }

            - **name (required):** Unique Category Name.

            - **code (required):** Unique Category Code.

            **Response:**
            
            - The API responds with a JSON array containing the following post details:
            
            - **detail**: Event category created successfuly.

        """
        return desc_val

    def get_operation_description_update():
        """
        Opration description
        """

        desc_val = """
            Update Event Category API
            -----------

            This API endpoint allows admin to Update Event Category.

            **Endpoint:** PUT event/categories/{cat_id}

            **Request Body:**

            - { "**name**": "string", "**code**": "string" }

            - **name (required):** Unique Category Name.

            - **code (required):** Unique Category Code.

            **URL Path Parameters:**
            
            - category_id (required): The unique identifier of the category.

            **Response:**
            
            - The API responds with a JSON array containing the following post details:
            
            - **detail**: Event category updated successfuly.

        """
        return desc_val

    def get_operation_description_delete():
        """
        Opration description
        """

        desc_val = """
            Delete Event Category API
            -----------

            This API endpoint allows admin to Delete Event Category.

            **Endpoint:** DELETE event/categories/{cat_id}

            **URL Path Parameters:**
            
            - category_id (required): The unique identifier of the category.

            **Response:**
            
            - The API responds with a JSON array containing the following post details:
            
            - **detail**: Event category deleted successfuly.

        """
        return desc_val

    def get_manual_parameters_create():
        """
        Manual input parameters for swagger ui
        """

        manual_parameters = [
            openapi.Parameter(
                "name",
                openapi.IN_FORM,
                description="Unique Category Name",
                type=openapi.TYPE_STRING,
                required=True,
            ),
            openapi.Parameter(
                "code",
                openapi.IN_FORM,
                description="Unique Category Code",
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ]
        return manual_parameters

    def get_manual_parameters_update():
        """
        Manual input parameters for swagger ui
        """

        manual_parameters = [
            openapi.Parameter(
                "name",
                openapi.IN_FORM,
                description="Unique Category Name",
                type=openapi.TYPE_STRING,
                required=True,
            ),
            openapi.Parameter(
                "code",
                openapi.IN_FORM,
                description="Unique Category Code",
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ]
        return manual_parameters

    def get_responses_list():
        """
        Response of the api
        """

        responses = {
            200: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "name": openapi.Schema(type=openapi.TYPE_STRING),
                        "code": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        }
        return responses

    def get_responses_detail():
        """
        Response of the api
        """

        responses = {
            200: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "name": openapi.Schema(type=openapi.TYPE_STRING),
                        "code": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        }
        return responses

    def get_responses_create():
        """
        Response of the api
        """

        responses = {
            201: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        }
        return responses

    def get_responses_update():
        """
        Response of the api
        """

        responses = {
            200: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        }
        return responses

    def get_responses_delete():
        """
        Response of the api
        """

        responses = {
            200: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        }
        return responses


class EventSchema:
    """
    Swagger attributes for Event
    """

    def get_tag():
        """
        Headline Tag
        """

        tag = ["Events (Admin)"]
        return tag

    def get_tag_common():
        """
        Headline Tag
        """

        tag = ["Events (Admin & User)"]
        return tag

    def get_operation_id_list():
        """
        Opration Unique ID
        """

        operation_id = "Event List"
        return operation_id

    def get_operation_id_detail():
        """
        Opration Unique ID
        """

        operation_id = "Event Details"
        return operation_id

    def get_operation_id_search():
        """
        Opration Unique ID
        """

        operation_id = "Search Event"
        return operation_id

    def get_operation_id_create():
        """
        Opration Unique ID
        """

        operation_id = "Admin - Create Event"
        return operation_id

    def get_operation_id_update():
        """
        Opration Unique ID
        """

        operation_id = "Admin - Update Event"
        return operation_id

    def get_operation_id_delete():
        """
        Opration Unique ID
        """

        operation_id = "Admin - Delete Event"
        return operation_id

    def get_opration_summary_list():
        """
        Opration sort summary
        """

        opration_summary = """Event List"""
        return opration_summary

    def get_opration_summary_detail():
        """
        Opration sort summary
        """

        opration_summary = """Event Details"""
        return opration_summary

    def get_opration_summary_create():
        """
        Opration sort summary
        """

        opration_summary = """Create Event"""
        return opration_summary

    def get_opration_summary_update():
        """
        Opration sort summary
        """

        opration_summary = """Update Event"""
        return opration_summary

    def get_opration_summary_delete():
        """
        Opration sort summary
        """

        opration_summary = """Delete Event"""
        return opration_summary

    def get_opration_summary_search():
        """
        Opration sort summary
        """

        opration_summary = """Search Event"""
        return opration_summary

    def get_operation_description_list():
        """
        Opration description
        """

        desc_val = """
            List Event API
            -----------

            This API endpoint allows to List Events.

            **Endpoint:** GET event/events/

            **Response:**
            
            - The API responds with a JSON array containing the following post details:
            
            - **id:** The unique identifier of the Event.

            - **title:** The title of the Event.

            - **description:** The description of the Event.

            - **category_id:** The category of the Event.

            - **max_seats:** Maximum avaliable seats of the Event.

            - **booking_start:** Booking start date of the Event.

            - **booking_end:** Booking end date of the Event.

            - **event_date:** Date of the Event.
        """
        return desc_val

    def get_operation_description_detail():
        """
        Opration description
        """

        desc_val = """
            Detail Event API
            -----------

            This API endpoint allows to get the details of the Event.

            **Endpoint:** GET event/events/{event_id}/

            **Response:**
            
            - The API responds with a JSON array containing the following post details:
            
            - **id:** The unique identifier of the Event.

            - **title:** The title of the Event.

            - **description:** The description of the Event.

            - **category_id:** The category of the Event.

            - **max_seats:** Maximum avaliable seats of the Event.

            - **booking_start:** Booking start date of the Event.

            - **booking_end:** Booking end date of the Event.

            - **event_date:** Date of the Event.

        """
        return desc_val

    def get_operation_description_create():
        """
        Opration description
        """

        desc_val = """
            Create Event API
            -----------

            This API endpoint allows admin to Create Event.

            **Endpoint:** POST event/events/

            **Request Body:**

            - { "**title**": "string", "**description**": "string", "**category_id**": "integer", \
                "**max_seats**": "integer", "**booking_start**": "datetime", "**booking_end**": "datetime", \
                "**event_date**": "datetime" }

            - **title (required):** Title of the event.

            - **description (required):** Description of the event.

            - **category_id (required):** Event category id.

            - **max_seats (required):** Maximum avaliable seats.

            - **booking_start (required):** Booking start date, **format**: YYYY-MM-DD.

            - **booking_end (required):** Booking end date, **format**: YYYY-MM-DD.

            - **event_date (required):** Event date, **format**: YYYY-MM-DD.

            **Response:**
            
            - The API responds with a JSON array containing the following post details:
            
            - **detail**: Event created successfuly.

        """
        return desc_val

    def get_operation_description_update():
        """
        Opration description
        """

        desc_val = """
            Update Event API
            -----------

            This API endpoint allows admin to Update Event.

            **Endpoint:** PUT event/events/{event_id}

            **Request Body:**

            - { "**title**": "string", "**description**": "string", "**category_id**": "integer", \
                "**max_seats**": "integer", "**booking_start**": "datetime", "**booking_end**": "datetime", \
                "**event_date**": "datetime" }

            - **title (required):** Title of the event.

            - **description (required):** Description of the event.

            - **category_id (required):** Event category id.

            - **max_seats (required):** Maximum avaliable seats.

            - **booking_start (required):** Booking start date, **format**: YYYY-MM-DD.

            - **booking_end (required):** Booking end date, **format**: YYYY-MM-DD.

            - **event_date (required):** Event date, **format**: YYYY-MM-DD.

            **URL Path Parameters:**
            
            - event_id (required): The unique identifier of the event.

            **Response:**
            
            - The API responds with a JSON array containing the following post details:
            
            - **detail**: Event updated successfuly.

        """
        return desc_val

    def get_operation_description_delete():
        """
        Opration description
        """

        desc_val = """
            Delete Event API
            -----------

            This API endpoint allows admin to Delete Event.

            **Endpoint:** DELETE event/events/{event_id}/

            **URL Path Parameters:**
            
            - event_id (required): The unique identifier of the event.

            **Response:**
            
            - The API responds with a JSON array containing the following post details:
            
            - **detail**: Event deleted successfuly.

        """
        return desc_val

    def get_operation_description_search():
        """
        Opration description
        """

        desc_val = """
            Search Event API
            -----------

            This API endpoint allows to search Events.

            **Endpoint:** GET event/search/events/

            **Request Parameters:**
            
            - **search:** The search query string used to find matching events.

            - This search based on event category, event title, event description, event date.

            - This parameter accepts partial matches and is case-insensitive.

            **Response:**
            
            - The API responds with a JSON array containing the following post details:
            
            - **id:** The unique identifier of the Event.

            - **title:** The title of the Event.

            - **description:** The description of the Event.

            - **category_id:** The category of the Event.

            - **max_seats:** Maximum avaliable seats of the Event.

            - **booking_start:** Booking start date of the Event.

            - **booking_end:** Booking end date of the Event.

            - **event_date:** Date of the Event.
        """
        return desc_val

    def get_manual_parameters_create():
        """
        Manual input parameters for swagger ui
        """

        manual_parameters = [
            openapi.Parameter(
                "title",
                openapi.IN_FORM,
                description="Event Title",
                type=openapi.TYPE_STRING,
                required=True,
            ),
            openapi.Parameter(
                "description",
                openapi.IN_FORM,
                description="Event Description",
                type=openapi.TYPE_STRING,
                required=True,
            ),
            openapi.Parameter(
                "category_id",
                openapi.IN_FORM,
                description="Event Category Id",
                type=openapi.TYPE_INTEGER,
                required=True,
            ),
            openapi.Parameter(
                "max_seats",
                openapi.IN_FORM,
                description="Avaliable Seats",
                type=openapi.TYPE_INTEGER,
                required=True,
            ),
            openapi.Parameter(
                "booking_start",
                openapi.IN_FORM,
                description="Booking Start Date",
                type=openapi.TYPE_STRING,
                required=True,
            ),
            openapi.Parameter(
                "booking_end",
                openapi.IN_FORM,
                description="Booking End Date",
                type=openapi.TYPE_STRING,
                required=True,
            ),
            openapi.Parameter(
                "event_date",
                openapi.IN_FORM,
                description="Event Date",
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ]
        return manual_parameters

    def get_manual_parameters_update():
        """
        Manual input parameters for swagger ui
        """

        manual_parameters = [
            openapi.Parameter(
                "title",
                openapi.IN_FORM,
                description="Event Title",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "description",
                openapi.IN_FORM,
                description="Event Description",
                type=openapi.TYPE_STRING,
                required=True,
            ),
            openapi.Parameter(
                "category_id",
                openapi.IN_FORM,
                description="Event Category Id",
                type=openapi.TYPE_INTEGER,
                required=True,
            ),
            openapi.Parameter(
                "max_seats",
                openapi.IN_FORM,
                description="Avaliable Seats",
                type=openapi.TYPE_INTEGER,
                required=True,
            ),
            openapi.Parameter(
                "booking_start",
                openapi.IN_FORM,
                description="Booking Start Date",
                type=openapi.TYPE_STRING,
                required=True,
            ),
            openapi.Parameter(
                "booking_end",
                openapi.IN_FORM,
                description="Booking End Date",
                type=openapi.TYPE_STRING,
                required=True,
            ),
            openapi.Parameter(
                "event_date",
                openapi.IN_FORM,
                description="Event Date",
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ]
        return manual_parameters

    def get_manual_parameters_search():
        """
        Manual input parameters for swagger ui
        """

        manual_parameters = [
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                description="Search text",
                type=openapi.TYPE_STRING,
            )
        ]
        return manual_parameters

    def get_responses_list():
        """
        Response of the api
        """

        responses = {
            200: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "title": openapi.Schema(type=openapi.TYPE_STRING),
                        "description": openapi.Schema(type=openapi.TYPE_STRING),
                        "category_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "max_seats": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "booking_start": openapi.Schema(type=openapi.TYPE_STRING),
                        "booking_end": openapi.Schema(type=openapi.TYPE_STRING),
                        "event_date": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        }
        return responses

    def get_responses_detail():
        """
        Response of the api
        """

        responses = {
            200: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "title": openapi.Schema(type=openapi.TYPE_STRING),
                        "description": openapi.Schema(type=openapi.TYPE_STRING),
                        "category_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "max_seats": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "booking_start": openapi.Schema(type=openapi.TYPE_STRING),
                        "booking_end": openapi.Schema(type=openapi.TYPE_STRING),
                        "event_date": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        }
        return responses

    def get_responses_create():
        """
        Response of the api
        """

        responses = {
            201: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        }
        return responses

    def get_responses_update():
        """
        Response of the api
        """

        responses = {
            200: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        }
        return responses

    def get_responses_delete():
        """
        Response of the api
        """

        responses = {
            200: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        }
        return responses


# Tickets
class EventTicketSchema:
    """
    Swagger attributes for Event Tickets
    """

    def get_tag():
        """
        Headline Tag
        """

        tag = ["Tickets (User)"]
        return tag

    def get_operation_id_list():
        """
        Opration Unique ID
        """

        operation_id = "User - Booked Event List"
        return operation_id

    def get_operation_id_detail():
        """
        Opration Unique ID
        """

        operation_id = "User - Ticket Details"
        return operation_id

    def get_operation_id_create():
        """
        Opration Unique ID
        """

        operation_id = "User - Book Ticket"
        return operation_id

    def get_opration_summary_list():
        """
        Opration sort summary
        """

        opration_summary = """Booked Event List"""
        return opration_summary

    def get_opration_summary_detail():
        """
        Opration sort summary
        """

        opration_summary = """Ticket Details"""
        return opration_summary

    def get_opration_summary_create():
        """
        Opration sort summary
        """

        opration_summary = """Book Ticket"""
        return opration_summary

    def get_operation_description_list():
        """
        Opration description
        """

        desc_val = """
            List Booked Event & Tickets API
            -----------

            This API endpoint allows user to list booked Events & Tickets.

            **Endpoint:** GET event/tickets/

            **Response:**
            
            - The API responds with a JSON array containing the following post details:
            
            - **user_id:** The unique identifier of the User.

            - **user_name:** Full name of the User.

            - **event_id:** The unique identifier of the Event.

            - **title:** The title of the Event.

            - **description:** The description of the Event.

            - **category:** The category of the Event.

            - **event_date:** Date of the Event.
            
            - **ticket_id:** The unique identifier of the Ticket.

            - **ticket_count:** Booked seats for the Event.

            - **boocked_at:** Boocked Date.
        """
        return desc_val

    def get_operation_description_detail():
        """
        Opration description
        """

        desc_val = """
            Detail Booked Event & Tickets API
            -----------

            This API endpoint allows user to get the details of the booked ticket.

            **Endpoint:** GET event/tickets/{ticket_id}/

            **Response:**
            
            - The API responds with a JSON array containing the following post details:
            
            - **user_id:** The unique identifier of the User.

            - **user_name:** Full name of the User.

            - **event_id:** The unique identifier of the Event.

            - **title:** The title of the Event.

            - **description:** The description of the Event.

            - **category:** The category of the Event.

            - **event_date:** Date of the Event.
            
            - **ticket_id:** The unique identifier of the Ticket.

            - **ticket_count:** Booked seats for the Event.

            - **boocked_at:** Boocked Date.

        """
        return desc_val

    def get_operation_description_create():
        """
        Opration description
        """

        desc_val = """
            Create Event API
            -----------

            This API endpoint allows user to Book Tickets.

            **Endpoint:** POST event/tickets/

            **Request Body:**

            - { "**user_id**": "integer", "**event_id**": "integer", "**ticket_count**": "integer"}

            - **user_id (required):** The unique identifier of the User.

            - **event_id (required):** The unique identifier of the Event.

            - **ticket_count (required):** Ticket Count.

            **Response:**
            
            - The API responds with a JSON array containing the following post details:
            
            - **detail**: Ticket booked successfuly.

        """
        return desc_val

    def get_responses_list():
        """
        Response of the api
        """

        responses = {
            200: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "user_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "user_name": openapi.Schema(type=openapi.TYPE_STRING),
                        "event_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "title": openapi.Schema(type=openapi.TYPE_STRING),
                        "description": openapi.Schema(type=openapi.TYPE_STRING),
                        "category": openapi.Schema(type=openapi.TYPE_STRING),
                        "event_date": openapi.Schema(type=openapi.TYPE_STRING),
                        "ticket_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "ticket_count": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "boocked_at": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        }
        return responses

    def get_responses_detail():
        """
        Response of the api
        """

        responses = {
            200: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "user_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "user_name": openapi.Schema(type=openapi.TYPE_STRING),
                        "event_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "title": openapi.Schema(type=openapi.TYPE_STRING),
                        "description": openapi.Schema(type=openapi.TYPE_STRING),
                        "category": openapi.Schema(type=openapi.TYPE_STRING),
                        "event_date": openapi.Schema(type=openapi.TYPE_STRING),
                        "ticket_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "ticket_count": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "boocked_at": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        }
        return responses

    def get_responses_create():
        """
        Response of the api
        """

        responses = {
            201: openapi.Response(
                "OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: "Bad Request",
            401: "Unauthorized",
            500: "Internal Server Error",
        }
        return responses
