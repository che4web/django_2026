from django.http import JsonResponse
from django.shortcuts import render, redirect
from urlshortapp.models import ShortUrl
from django.views.generic.list import ListView


# Галавная страница
def index(request):
    urls = ShortUrl.objects.all()

    search = request.GET.get("search")
    if search:
        urls = urls.filter(source_url__icontains=search)
    context = {
        "urls": urls,
    }
    return render(request, "index.html", context)


# Галавная страница
def index_json(request):
    urls = ShortUrl.objects.all()

    search = request.GET.get("search")
    if search:
        urls = urls.filter(source_url__icontains=search)
    data = list(urls.values("id", "source_url", "short_url"))
    return JsonResponse(data=data, safe=False)


class ShortUrlsList(ListView):
    model = ShortUrl


# Седирект на исходный url.
def redirect_url(request, short_url):

    obj = ShortUrl.objects.get(short_url=short_url)
    return redirect(obj.source_url)


# Форма создания нового url.
def create_url(request):
    if request.POST:
        source_url = request.POST.get("source_url")
        sh, created = ShortUrl.objects.get_or_create(
            source_url=source_url,
        )
        if created:
            sh.gen_short_url()
            sh.save()

    return redirect("/")
