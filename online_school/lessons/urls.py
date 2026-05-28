from django.urls import path

from .views import lesson_list_view, lesson_create_view

urlpatterns = [
    path('', lesson_list_view, name="home"),
    path('lessons/create/', lesson_create_view, name="lesson-create")
]
