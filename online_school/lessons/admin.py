from django.contrib import admin
from .models import Lesson, LessonMaterial, LessonVideo, LessonVideoProgress

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

@admin.register(LessonVideo)
class LessonVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(LessonVideoProgress)
class LessonVideoProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'video', 'last_position_seconds', 'duration_seconds', 'is_completed', 'completed_at', 'updated_at')
