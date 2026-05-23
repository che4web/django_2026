#import "@preview/slydst:0.1.5": *

#show: slides.with(
  title: "Django Vue Lab",
  subtitle: "Занятие 2. Backend разработка, MVC",
  authors: "Черепанов И.Н. Филипьев В.А.",
  subslide-numbering: "(i)",
)

#show raw: set block(fill: silver.lighten(65%), width: 100%, inset: 1em)

== Backend серверная разработка

#figure(image("img/main-qimg-09f5cf57e8c9de343282f1fa84f33345.jpg", width: 80%))


== Backend

- web-сервер
- Бизнес логика
- Базы данных


== Основные подходы

- Статические страницы (HTML -- без программирования)
- Динамические страницы -- требуют программирования
  - Писать с нуля - лучше не делать 
  - *Framework*
     - Django
     - Flask
     - FastApi
     - Ruby on Rails
     - Laravel
     - Express
  - CMS 
    - Wordpress
    - Bitrix
    - DjagnoCMS
    - ...


== На чем писать?

- PHP
- Perl
- C\#
- *Python*
- Java
- JavaScript
- *Go*
- *Rust*
- и прочие...


== Способы реализации серверной части

- Внедрить код в web-сервер
- Использовать модули
- CGI
- fastCGI
- *WSGI*
- *ASGI*


== CGI

```python
import os
import sys

print("Content-type: text/html")
print("Status: 200")
print("")
print("<h1>Hello world!</h1>")

```
== Пример Запрос - Ответ
```http

 GET /cgi-bin/index.py HTTP/1.1
> Host: localhost:8001
> User-Agent: curl/8.20.0
> Accept: */*
>
* Request completely sent off
* HTTP 1.0, assume close after body
< HTTP/1.0 200 Script output follows
< Server: SimpleHTTP/0.6 Python/3.14.5
< Date: Fri, 22 May 2026 13:00:43 GMT
< Content-Type: text/html; charset=utf-8
<
<h1>Hello world!</h1>
```


== MVC

Model-View-Controller (*MVC*, «Модель-Представление-Контроллер») — схема разделения данных приложения, пользовательского интерфейса и управляющей логики на три отдельных компонента: модель, представление и контроллер — таким образом, что модификация каждого компонента может осуществляться независимо.

- *Модель* (Model) предоставляет данные и реагирует на команды контроллера, изменяя свое состояние
- *Представление* (View) отвечает за отображение данных модели пользователю, реагируя на изменения модели
- *Контроллер* (Controller) интерпретирует действия пользователя, оповещая модель о необходимости изменений


== MVC
#grid(
  columns:(1fr,1fr),
[
- *Model* -- работа с данными (БД)
- *Controller* -- логика работы
- *View* -- как выглядит
- Роутинг -- соответствие запроса контроллеру


],[

#figure(image("img/240px-MVC-Process.png", width: 100%))
]
)

== Django

Django (Джанго) — свободный фреймворк для веб-приложений на языке Python, использующий шаблон проектирования MVC. Проект поддерживается организацией Django Software Foundation.

- Model -- Model
- Controller -- View
- View -- Template


== Django

```python
from django.db import models

class Article(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='название',
    )
    discript = models.CharField(
        verbose_name='описание',
        max_length=255,
    )
```


== ORM

SQL -- не нужен?

ORM (англ. Object-Relational Mapping, объектно-реляционное отображение)

```bash
./manage.py makemigrations
./manage.py migrate
```

```python
art_list = Article.objects.filter(name='Test')
art = Article(name='Test', description='test')
art.save()
```

```python
art = Article()
art.name = 'test'
art.description = 'test'
art.save()
```


== View

View - функция принимает HttpRequest, Возвращает HttpResponse

```python
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
```

== View
```python
from django.shortcuts import render

def detail(request, article_id):
    art = Article.objects.get(pk=poll_id)
    return render(request,'article/detail.html', {'article': art})
```
Классовые view
```python
class ArticleDetailView(DetailView):
    model = Article
```


== Routing

Какая функция отработает на каком URL? *urls.py*

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/([0-9]{4})/$', views.year_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
]
```
== Routing
```python
from django.urls import path

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```
== Шаблоны

Шаблоны содержат статический HTML и динамические данные, рендеринг которых описан специальным синтаксисом.


```html
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
<li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

```python
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

== Шаблоны
- язык шаблонов похож на jinja2 
- шаблоны могу наследоваться
- избегайте hadr-code url
- Можно вызывать функции без параметров
- tags
- filters 
- request
- После отрисовки передается пользователю
- нет связи с сервером.

==

#v(1fr)
#align(center)[
  #text(size: 1.8em, fill: default-color)[*Спасибо за внимание*]

  #v(0.6em)
  #text(size: 0.65em)[Квест завершен]

  #text(size: 0.65em )[Новая цель: перейти к вопросам]
]
#v(1fr)
