from rest_framework import serializers

from .models import User

class CurrentUserSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(source="get_full_name", read_only=True)
    is_teacher = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "full_name",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "avatar",
            'is_teacher'
        )
    def get_is_teacher(self, obj):
        return bool(obj.is_superuser or hasattr(obj, 'teacherprofile'))
