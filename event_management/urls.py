"""
URL configuration for event_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# pylint: disable=C0103
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from rest_framework import permissions


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="EVENT MANAGEMENT APP",
        default_version='v1',
        description="""
            Description
            -----------

            The developed APIs for the event management platform provide a comprehensive set of functionalities to allow users to 
            create accounts, log in and out, view active event list, book & viewmtickets for the event, 
            search events by category, title, description or event date, and provide an admin(**http://127.0.0.1:8000/admin/**) 
            interface for create and manage events, and categories under **Event** table. also provided **personalized APIs** for **sensitive admin oprations**. 

            NOTE - Developers: Basicaly we are not allowing creat admin automatically, so plese makse sure that have admin account or create one **Superuser**.

            - The APIs are designed to be user-friendly, secure, and efficient. They handle various error scenarios and provide appropriate error responses to 
            ensure data integrity and smooth user experience. The implementation includes unit tests to verify the correctness and functionality of the APIs.

            - To facilitate API usage and integration, comprehensive API documentation is provided using Swagger. The documentation includes detailed descriptions, 
            request and response examples, and clear instructions on how to interact with each API endpoint.

            - In conclusion, the developed APIs for the social media platform offer a robust and scalable solution for building a social media application, 
            enabling users to connect, share, and interact within the platform's ecosystem.
        
            Authorize
            ---------
            
            - please provide your AUTH-TOEN to Authorize swagger function (**format: Token {YOUR TOKEN}**) for further api access.

            **Thankyou**
        """,
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/event/', include('apps.events.urls')),
    path('api/account/', include('apps.accounts.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
