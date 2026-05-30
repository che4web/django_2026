from django.contrib import admin
from .models import Lesson, LessonMaterial

class LessonMaterialInline(admin.TabularInline):
    model = LessonMaterial
    extra = 1

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_filter = ("lesson_type", "is_published")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = (LessonMaterialInline, )

@admin.register(LessonMaterial)
class LessonMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

