from django.shortcuts import render
from urlshortapp.models import ShortUrl


# Create your views here.
def index(request):
    urls = ShortUrl.objects.all()
    context = {
        "urls": urls,
    }
    return render(request, "index.html", context)


# Create your views here.
def create_url(request):
    context = {}
    if request.POST:
        source_url = request.POST.get("source_url")
        short_url = request.POST.get("short_url")
        if source_url and short_url:
            sh = ShortUrl(
                source_url=source_url,
                short_url=short_url,
            )
            sh.save()

    return render(request, "url_form.html", context)
