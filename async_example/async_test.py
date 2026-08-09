import httpx
import time
import asyncio


async def main():
    client = httpx.Client()

    start = time.time()
    for x in range(10):
        data = client.get(f"http://127.0.0.1:8000?name={x}")
    print(time.time() - start)

    async_client = httpx.AsyncClient()

    start = time.time()
    task = []
    for x in range(10):
        t = async_client.get(f"http://127.0.0.1:8000?name={x}")
        task.append(t)
    await asyncio.gather(*task)
    print(time.time() - start)


asyncio.run(main())
