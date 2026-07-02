from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from .models import User
from .serializers import CurrentUserSerializer, TeacherSerializer


class UserViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = TeacherSerializer

    @action(detail=False, methods=["get"], url_path="teachers")
    def get_teacher(self, request):
        teachers = self.queryset.filter(
            Q(teacher_profile__isnull=False) | Q(is_superuser=True)
        ).distinct()
        serializer = self.get_serializer(teachers, many=True)
        return Response(serializer.data)


@method_decorator(ensure_csrf_cookie, name="dispatch")
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
