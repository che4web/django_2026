from .models import Lesson, LessonType, LessonMaterial, LessonVideo
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class LessonMaterialSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = LessonMaterial


class LessonVideoSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "title", "file", "position", "lesson")
        model = LessonVideo


class LessonSerializer(ModelSerializer):
    lesson_type_display = serializers.CharField(
        source="get_lesson_type_display", read_only=True
    )
    teacher_name = serializers.SerializerMethodField()
    materials = LessonMaterialSerializer(many=True, read_only=True)
    videos = LessonVideoSerializer(many=True, read_only=True)

    def get_teacher_name(self, obj):
        if not obj.teacher:
            return ""
        return obj.teacher.get_full_name()

    class Meta:
        fields = (
            "id",
            "title",
            "lesson_type",
            "lesson_type_display",
            "is_published",
            "slug",
            "description",
            "position",
            "duration_minutes",
            "lesson_date",
            "image",
            "teacher",
            "teacher_name",
            "materials",
            "videos",
        )
        model = Lesson
