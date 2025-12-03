import asyncio


async def sort_val(val):
    await asyncio.sleep(val)
    print(val, end=" ", flush=True)


async def sleep_sort(values):
    tasks = [sort_val(v) for v in values]
    await asyncio.gather(*tasks)


n = [4, 7, 1, 2, 1]
asyncio.run(sleep_sort(n))
