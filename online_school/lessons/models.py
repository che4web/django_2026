from django.db import models


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

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ("position",)

    def __str__(self):
        return self.title


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
