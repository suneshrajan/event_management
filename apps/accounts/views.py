"""Module imports"""
# pylint: disable=E0401, R0205, R0903, E1101, W0718
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from drf_yasg.utils import swagger_auto_schema
from utils.swgr_doc_schmas import SignupSchema, LoginSchema, LogOutSchema

from apps.accounts.models import User
from apps.accounts.serializers import UserSerializer, UserProfileSerializer


class UserSignup(APIView):
    """
    User signup - register users
    """

    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        security=[],
        tags=SignupSchema.get_tag(),
        operation_id=SignupSchema.get_operation_id(),
        operation_summary=SignupSchema.get_opration_summary(),
        operation_description=SignupSchema.get_operation_description(),
        manual_parameters=SignupSchema.get_manual_parameters(),
        consumes=SignupSchema.get_consumes(),
        responses=SignupSchema.get_responses(),
    )
    def post(self, request):
        """
        User signup - register users
        """

        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                # Create User
                serializer.save()

                # Password hashing
                user = User.objects.get(email=request.data["email"])
                user.set_password(request.data["password"])
                user.save()

                # Create token
                token = Token.objects.create(user=user)

                # Auth user details
                user_data = UserProfileSerializer(user).data
                return Response(
                    {
                        "token": token.key,
                        "data": user_data,
                        "detail": "User created successfully.",
                    },
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UserLogin(APIView):
    """
    User login - signin users
    """

    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        security=[],
        tags=LoginSchema.get_tag(),
        operation_id=LoginSchema.get_operation_id(),
        operation_summary=LoginSchema.get_opration_summary(),
        operation_description=LoginSchema.get_operation_description(),
        manual_parameters=LoginSchema.get_manual_parameters(),
        responses=LoginSchema.get_responses(),
    )
    def post(self, request):
        """
        User login - signin users
        """

        try:
            try:
                user = User.objects.get(email=request.data["email"])
            except User.DoesNotExist:
                return Response(
                    {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
                )

            # Validating username and password
            if not user.check_password(request.data["password"]):
                return Response(
                    {"detail": "User password wrong."}, status=status.HTTP_404_NOT_FOUND
                )

            # Generate Token for auth user
            token, created = Token.objects.get_or_create(user=user)

            # Auth user details
            user_data = UserProfileSerializer(user).data
            result = {
                "token": "Token " + token.key,
                "data": user_data,
                "detail": "User login successful",
            }
            return Response(result, status=status.HTTP_200_OK)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UserLogout(APIView):
    """
    User logout - signout users
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=LogOutSchema.get_tag(),
        operation_id=LogOutSchema.get_operation_id(),
        operation_summary=LogOutSchema.get_opration_summary(),
        operation_description=LogOutSchema.get_operation_description(),
        responses=LogOutSchema.get_responses(),
    )
    def get(self, request):
        """
        User logout - signout users
        """
        try:
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            user.auth_token.delete()
            return Response("Successful logout", status=status.HTTP_200_OK)
        except Exception as _e:
            return Response(
                f"Somthing went wrong: {_e}",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
