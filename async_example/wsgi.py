import time
import json

from urllib.parse import parse_qs


def app(environ, start_response):
    params = parse_qs(environ.get("QUERY_STRING", ""))

    name = params.get("name", ["unknown"])[0]
    print(f"start client {name}")
    time.sleep(1)

    body = f"name={name}".encode()

    start_response("200 OK", [("Content-Type", "text/plain")])

    print(f"end client {name}")
    print(f"==========")
    return [body]
