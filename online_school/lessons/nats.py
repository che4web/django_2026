import asyncio
import nats
from nats.aio.client import Client as NATS


_nc: NATS | None = None
_lock = asyncio.Lock()


async def get_nats() -> NATS:
    global _nc

    if _nc is not None and _nc.is_connected:
        return _nc

    async with _lock:
        # Пока ждали lock, другой coroutine мог уже подключиться
        if _nc is not None and _nc.is_connected:
            return _nc

        _nc = await nats.connect(
            servers=["nats://127.0.0.1:4222"],
            name="django",
            allow_reconnect=True,
            max_reconnect_attempts=-1,
            reconnect_time_wait=2,
        )

        return _nc
