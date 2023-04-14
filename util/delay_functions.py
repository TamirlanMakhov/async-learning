import asyncio


async def delay(delay_seconds):
    print(f'засыпаю на {delay_seconds} сек')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} сек завершен')
    return delay_seconds
