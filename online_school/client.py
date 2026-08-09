import os
import asyncio


import nats
from nats.errors import TimeoutError

servers = os.environ.get("NATS_URL", "nats://localhost:4222").split(",")


async def main():

    nc = await nats.connect(servers=servers)

    sub = await nc.subscribe("test_room")
    async for msg in sub.messages:
        print(msg)


if __name__ == "__main__":
    asyncio.run(main())
