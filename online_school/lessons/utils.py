from slugify import slugify


def generate_unique_lesson_slug(title, exclude_pk=None):
    from .models import Lesson

    base_slug = slugify(title) or "lesson"
    slug = base_slug
    counter = 1
    while True:
        queryset = Lesson.objects.filter(slug=slug)
        if exclude_pk:
            queryset = queryset.exclude(pk=exclude_pk)
        if not queryset.exists():
            return slug
        slug = f"{base_slug}-{counter}"
        counter += 1
