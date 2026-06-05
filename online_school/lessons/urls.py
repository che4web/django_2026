from django.urls import path

from .views import lesson_list_view, lesson_create_view, LessonListView, LessonDetailView, LessonCreateView,LessonListJSONView,LessonListFetchView

urlpatterns = [
    # path('', lesson_list_view, name="home"),
    path('', LessonListView.as_view(), name="home"),
    path('lessons/create/', LessonCreateView.as_view(), name="lesson-create"),
    path('lessons/lesson-json/',LessonListJSONView.as_view(), name="lesson-json" ),
    path('lessons/lessons-fetch/', LessonListFetchView.as_view(), name="lesson-fetch"),
    path('lessons/<slug:slug>/', LessonDetailView.as_view(), name="lesson-detail"),
    # path('lessons/create/', lesson_create_view, name="lesson-create")
]
