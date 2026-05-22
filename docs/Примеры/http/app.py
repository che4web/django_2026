from django.conf import settings
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

settings.configure(
    DEBUG=True,
    SECRET_KEY="dev",
    ROOT_URLCONF=__name__,
    INSTALLED_APPS=[],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    },
    ALLOWED_HOSTS=["*"],
)

import django

django.setup()

from django.db import connection, models
from django.http import HttpResponse
from django.urls import path


# модель
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        app_label = "single_file_app"

    def __str__(self):
        return self.name


def create_tables():
    if User._meta.db_table in connection.introspection.table_names():
        return

    with connection.schema_editor() as schema_editor:
        schema_editor.create_model(User)


# маршрут
def index(request):
    create_tables()

    if not User.objects.exists():
        User.objects.create(
            name="Ivan",
            age=30,
        )

    rows = User.objects.all()

    text = "<br>".join(f"{u.name}: {u.age}" for u in rows)

    return HttpResponse(text)


urlpatterns = [
    path("", index),
]


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line()
