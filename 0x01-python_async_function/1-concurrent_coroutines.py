#!/usr/bin/env python3
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random

async def wait_n(n, max_delay):
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        insert_pos = 0
        while insert_pos < len(delays) and delays[insert_pos] < delay:
            insert_pos += 1
        delays.insert(insert_pos, delay)
    return delays
