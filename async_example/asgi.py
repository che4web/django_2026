# app.py

import asyncio
from urllib.parse import parse_qs
import time


async def app(scope, receive, send):
    if scope["type"] != "http":
        return

    # В ASGI query_string приходит как bytes
    query_string = scope.get("query_string", b"").decode()
    params = parse_qs(query_string)

    name = params.get("name", ["unknown"])[0]

    print(f"start client {name}")

    # Неблокирующая задержка
    await asyncio.sleep(1)

    body = f"name={name}".encode()

    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [
                (b"content-type", b"text/plain"),
            ],
        }
    )

    await send(
        {
            "type": "http.response.body",
            "body": body,
        }
    )

    print(f"end client {name}")
    print("==========")
