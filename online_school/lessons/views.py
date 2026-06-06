from django.forms import fields
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Lesson, LessonType, LessonMaterial
from online_school.forms_utils import apply_bootstrap_classes
from .forms import LessonForm, LessonMaterialFormSet
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as filters

from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .serializers import LessonSerializer, LessonMaterialSerializer


class LessonFilter(filters.FilterSet):
    search = filters.CharFilter(method="get_search2")

    def get_search2(self, queryset, name, value):
        if value:
            queryset = queryset.filter(
                Q(title__icontains=value) | Q(description__icontains=value)
            )
        return queryset

    class Meta:
        model = Lesson
        exclude = ["file"]


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LessonFilter


class LessonMaterialFilter(filters.FilterSet):
    class Meta:
        model = LessonMaterial
        exclude = ["file"]


class LessonMaterialViewSet(ModelViewSet):
    queryset = LessonMaterial.objects.all()
    serializer_class = LessonMaterialSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LessonMaterialFilter


class LessonListFetchView(TemplateView):
    template_name = "lesson_list_fetch.html"


class LessonListJSONView(ListView):
    model = Lesson

    def get_queryset(self):
        lessons = Lesson.objects.filter(is_published=True)
        lessons_type = self.request.GET.get("lesson_type")
        if lessons_type:
            lessons = lessons.filter(lesson_type=lessons_type)
        return lessons

    def render_to_response(self, context, **response_kwargs):
        lessons = context["object_list"]
        data = []

        for lesson in lessons:
            data.append(
                {
                    "id": lesson.id,
                    "title": lesson.title,
                    "slug": lesson.slug,
                    "description": lesson.description,
                    "lesson_type": lesson.lesson_type,
                    "lesson_type_display": lesson.get_lesson_type_display(),
                    "position": lesson.position,
                }
            )
        return JsonResponse(data, safe=False)


def lesson_list_view(request):
    lessons = Lesson.objects.filter(is_published=True)
    context = {"lessons": lessons}
    return render(request, "lesson_list.html", context)


class LessonListView(ListView):
    model = Lesson
    template_name = "lesson_list.html"
    context_object_name = "lessons"

    def get_queryset(self):
        lessons = Lesson.objects.filter(is_published=True)
        lesson_type = self.request.GET.get("lesson_type")

        if lesson_type:
            lessons = lessons.filter(lesson_type=lesson_type)

        return lessons

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected_lesson_type"] = self.request.GET.get("lesson_type", "")
        context["lesson_types"] = LessonType.choices
        return context


class LessonDetailView(DetailView):
    model = Lesson
    template_name = "lesson_detail.html"
    context_object_name = "lesson"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Lesson.objects.filter(is_published=True)


class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = "lesson_form.html"
    success_url = reverse_lazy("home")


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
