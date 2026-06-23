from django.db import models
from django.urls import reverse
from django.conf import settings
class LessonType(models.TextChoices):
    THEORY = "theory", "Теория"
    PRACTICE = (
        "practice",
        "Практика",
    )
    ONLINE = "live", "Онлайн"


class MaterialType(models.TextChoices):
    FILE = "file", "Файл"
    LINK = "link", "Ссылка"


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="Слаг")
    description = models.TextField(blank=True, verbose_name="Описание")
    lesson_type = models.CharField(
        choices=LessonType.choices, default=LessonType.THEORY, blank=True, verbose_name="Тип урока"
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликован")
    position = models.PositiveIntegerField(default=1, verbose_name="Позиция")
    file = models.FileField(upload_to="lessons/file", blank=True, null=True)
    duration_minutes = models.PositiveIntegerField(default=1, verbose_name="Длительность в минутах")
    lesson_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата урока")
    image = models.ImageField(upload_to="lessons/image", blank=True, null=True, verbose_name="Превью урока")
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="lessons", verbose_name="Преподаватель", blank=True, null=True)
    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ("position",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("lesson-detail", kwargs={"slug": self.slug})
class LessonMaterial(models.Model):
    lesson = models.ForeignKey(
        "lessons.Lesson",
        on_delete=models.CASCADE,
        related_name="materials",
        verbose_name="Урок",
    )
    material_type = models.CharField(
        choices=MaterialType.choices,
        default=MaterialType.FILE,
        max_length=10,
        verbose_name="Тип материала",
    )
    file = models.FileField(upload_to="lesson_materials/", blank=True, verbose_name="Файл")
    url = models.URLField(blank=True, verbose_name="Ссылка")
    position = models.PositiveIntegerField(default=1, verbose_name="Позиция")
    title = models.CharField(max_length=255, verbose_name="Название")
    text = models.TextField(blank=True, verbose_name="Текст")

    class Meta:
        verbose_name = "Материал урока"
        verbose_name_plural = "Материалы уроков"

    def __str__(self):
        return self.title

class LessonVideo(models.Model):
    lesson = models.ForeignKey(
        "lessons.Lesson",
        on_delete=models.CASCADE,
        related_name="videos",
        verbose_name="Урок",
    )
    file = models.FileField(upload_to="lessons/videos/", blank=True, null=True, verbose_name="Видео")
    title = models.CharField(max_length=255, verbose_name="Название")
    position = models.PositiveIntegerField(default=1, verbose_name="Позиция")

    class Meta:
        verbose_name = "Видео урока"
        verbose_name_plural = "Видео уроков"
        ordering = ("position",)

    def __str__(self):
        return self.title

class LessonVideoProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="lesson_video_progress", verbose_name="Пользователь")
    video = models.ForeignKey(LessonVideo, on_delete=models.CASCADE, related_name="progress", verbose_name="Видео")
    last_position_seconds = models.PositiveIntegerField(default=0, verbose_name="Последняя позиция в секундах")
    duration_seconds = models.PositiveIntegerField(default=0, verbose_name="Длительность в секундах")
    is_completed = models.BooleanField(default=False, verbose_name="Завершено")
    completed_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата завершения")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Прогресс просмотра видео урока"
        verbose_name_plural = "Прогресс просмотра видео уроков"
        ordering = ("updated_at",)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.video.title}"
