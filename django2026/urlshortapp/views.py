from django.shortcuts import render, redirect
from urlshortapp.models import ShortUrl
import hashlib
import base64


# Create your views here.
def index(request):
    urls = ShortUrl.objects.all()
    context = {
        "urls": urls,
    }
    return render(request, "index.html", context)


def redirect_url(request, short_url):
    obj = ShortUrl.objects.get(short_url=short_url)
    return redirect(obj.source_url)


# Create your views here.
def create_url(request):
    context = {}
    if request.POST:
        source_url = request.POST.get("source_url")
        short_url = hashlib.sha256(source_url.encode()).digest()
        short_url = base64.urlsafe_b64encode(short_url).decode()
        short_url = short_url[:6]
        if not ShortUrl.objects.filter(short_url=short_url).exists():
            sh = ShortUrl(
                source_url=source_url,
                short_url=short_url[:6],
            )
            sh.save()
    return redirect("/")
