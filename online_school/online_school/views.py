import mimetypes
import os

from django.conf import settings
from django.http import FileResponse, Http404, StreamingHttpResponse
from django.utils._os import safe_join
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def vue_app(request):
    return render(request, "index.html")

def serve_media(request, path):
    full_path = safe_join(settings.MEDIA_ROOT, path)
    if not os.path.isfile(full_path):
        raise Http404("Media not found")

    content_type, encoding = mimetypes.guess_type(full_path)
    content_type = content_type or "application/octet-stream"
    file_size = os.path.getsize(full_path)
    range_header = request.headers.get("Range", "")

    if not range_header.startswith("bytes="):
        response = FileResponse(open(full_path, "rb"), content_type=content_type)
        response["Accept-Ranges"] = "bytes"
        if encoding:
            response["Content-Encoding"] = encoding
        return response

    start_raw, _, end_raw = range_header.removeprefix("bytes=").partition("-")
    start = int(start_raw) if start_raw else 0
    end = int(end_raw) if end_raw else file_size - 1
    length = end - start + 1

    def stream():
        with open(full_path, "rb") as file:
            file.seek(start)
            remaining = length
            while remaining > 0:
                chunk = file.read(min(8192, remaining))
                if not chunk:
                    break
                remaining -= len(chunk)
                yield chunk

    response = StreamingHttpResponse(stream(), status=206, content_type=content_type)
    response["Accept-Ranges"] = "bytes"
    response["Content-Length"] = str(length)
    response["Content-Range"] = f"bytes {start}-{end}/{file_size}"
    if encoding:
        response["Content-Encoding"] = encoding
    return response
