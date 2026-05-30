from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Lesson, LessonType
from online_school.forms_utils import apply_bootstrap_classes

from .forms import LessonForm, LessonMaterialFormSet


def lesson_list_view(request):
    lessons = Lesson.objects.filter(is_published=True)
    context = {"lessons": lessons}
    return render(request, "lesson_list.html", context)


@ensure_csrf_cookie
def lesson_create_view(request):
    if request.method == "POST":
        form = LessonForm(request.POST, request.FILES)
        formset = LessonMaterialFormSet(request.POST, request.FILES)

        apply_bootstrap_classes(form)
        for material_form in formset:
            apply_bootstrap_classes(material_form)

        if form.is_valid() and formset.is_valid():
            lesson = form.save()
            formset.instance = lesson
            formset.save()
            return redirect("home")
    else:
        form = LessonForm(initial={"is_published": True})
        formset = LessonMaterialFormSet()

        apply_bootstrap_classes(form)
        for material_form in formset:
            apply_bootstrap_classes(material_form)

    return render(
        request,
        "lesson_form.html",
        {
            "form": form,
            "formset": formset,
        },
    )


def lesson_create_view_manual(request):
    errors = {}
    values = {
        "title": "",
        "slug": "",
        "description": "",
        "position": "1",
        "lesson_type": LessonType.THEORY,
        "is_published": False,
    }

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        slug = request.POST.get("slug", "").strip()
        description = request.POST.get("description", "").strip()
        position_raw = request.POST.get("position", "").strip()
        lesson_type = request.POST.get("lesson_type")
        is_published = request.POST.get("is_published") == "on"
        file = request.FILES.get("file")

        values = {
            "title": title,
            "slug": slug,
            "description": description,
            "position": position_raw,
            "lesson_type": lesson_type,
            "is_published": is_published,
        }

        if not title:
            errors["title"] = "Введите название урока."

        if not slug:
            errors["slug"] = "Введите слаг."
        elif Lesson.objects.filter(slug=slug).exists():
            errors["slug"] = "Урок с таким слагом уже существует."

        if not position_raw:
            errors["position"] = "Введите позицию урока."
        else:
            try:
                position = int(position_raw)
            except ValueError:
                errors["position"] = "Позиция должна быть числом."
            else:
                if position < 1:
                    errors["position"] = "Позиция должна быть больше нуля."

        lesson_type_values = [choice[0] for choice in LessonType.choices]
        if lesson_type not in lesson_type_values:
            errors["lesson_type"] = "Выберите корректный тип урока."

        if not errors:
            Lesson.objects.create(
                title=title,
                slug=slug,
                description=description,
                position=position,
                lesson_type=lesson_type,
                is_published=is_published,
                file=file,
            )
            return redirect("home")

    context = {
        "errors": errors,
        "values": values,
        "lesson_type_choices": LessonType.choices,
    }
    return render(request, "lesson_form.html", context)
