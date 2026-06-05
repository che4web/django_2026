from django import forms
from django.forms import inlineformset_factory
from .models import Lesson, LessonMaterial
from online_school.forms_utils import apply_bootstrap_classes

class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_bootstrap_classes(self)

class LessonForm(BootstrapModelForm):
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
