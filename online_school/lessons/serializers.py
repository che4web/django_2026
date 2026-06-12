from .models import Lesson, LessonType, LessonMaterial
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class LessonSerializer(ModelSerializer):
    lesson_type_display = serializers.CharField(source="get_lesson_type_display", read_only=True)
    class Meta:
        fields = (
            "id",
            "title",
            "lesson_type",
            "lesson_type_display",
            "is_published",
            "slug",
            "description",
            "position"
        )
        model = Lesson


class LessonMaterialSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = LessonMaterial
