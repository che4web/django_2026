from .models import Lesson, LessonType, LessonMaterial
from rest_framework.serializers import ModelSerializer


class LessonSerializer(ModelSerializer):
    class Meta:
        # fields = "__all__"
        exclude = ["lesson_type"]
        model = Lesson


class LessonMaterialSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = LessonMaterial
