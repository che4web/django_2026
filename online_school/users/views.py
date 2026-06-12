from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import CurrentUserSerializer


class CurrentUserView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if not request.user.is_authenticated:
            return Response({"is_authenticated": False, "user": None})

        return Response(
            {
                "is_authenticated": True,
                "user": CurrentUserSerializer(
                    request.user, context={"request": request}
                ).data,
            }
        )
