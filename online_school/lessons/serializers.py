from .models import Lesson, LessonType, LessonMaterial, LessonVideo, LessonTest, TestQuestion, TestAnswer
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

class TestAnswerPublicSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "text",)
        model = TestAnswer

class TestQuestionPublicSerializer(ModelSerializer):
    answers = TestAnswerPublicSerializer(many=True, read_only=True)

    class Meta:
        fields = ("id", "text", "answers", "position")
        model = TestQuestion

class LessonTestPublicSerializer(ModelSerializer):
    questions = TestQuestionPublicSerializer(many=True, read_only=True)

    class Meta:
        fields = ("id", "title", "passing_score", "is_published", "questions")
        model = LessonTest
class LessonSerializer(ModelSerializer):
    lesson_type_display = serializers.CharField(
        source="get_lesson_type_display", read_only=True
    )
    teacher_name = serializers.SerializerMethodField()
    materials = LessonMaterialSerializer(many=True, read_only=True)
    videos = LessonVideoSerializer(many=True, read_only=True)
    tests = LessonTestPublicSerializer(many=True, read_only=True)
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
            "tests",
        )
        model = Lesson

class LessonTestSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "title", "passing_score", "is_published")
        model = LessonTest

class TestQuestionSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "text", "position")
        model = TestQuestion

class TestAnswerSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "text", "is_correct", "position")
        model = TestAnswer


