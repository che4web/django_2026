from django import forms
from django.forms import inlineformset_factory
from .models import Lesson, LessonMaterial


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = (
            "title",
            "slug",
            "description",
            "position",
            "is_published",
            "lesson_type",
            "file",
        )


class LessonMaterialForm(forms.ModelForm):
    class Meta:
        model = LessonMaterial
        fields = (
            "title",
            "material_type",
            "file",
            "url",
            "text",
            "position",
        )

LessonMaterialFormSet = inlineformset_factory(
    Lesson,
    LessonMaterial,
    form=LessonMaterialForm,
    extra=1,
    can_delete=False,
)
