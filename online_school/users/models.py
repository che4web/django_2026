from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=32, blank=True, verbose_name="Телефон")
    avatar = models.ImageField(upload_to="users/avatars/", blank=True, verbose_name='Аватар')

    class Meta(AbstractUser.Meta):
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class StudentProfile(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="student_profile",
        verbose_name="Пользователь"
    )
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата Рождения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    class Meta:
        verbose_name = 'Профиль студента'
        verbose_name_plural = 'Профили студентов'

    def __str__(self):
        return self.user.get_full_name()

class TeacherProfile(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="teacher_profile",
        verbose_name="Пользователь"
    )
    bio = models.TextField(blank=True, verbose_name="О себе")
    expertise = models.CharField(max_length=255, blank=True, verbose_name="Экспертиза")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    class Meta:
        verbose_name = 'Профиль преподователя'
        verbose_name_plural = 'Профили преподавателей'

    def __str__(self):
        return self.user.get_full_name()
