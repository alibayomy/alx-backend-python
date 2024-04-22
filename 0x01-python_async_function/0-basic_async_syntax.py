#!/usr/bin/env python3
import random
import asyncio


async def wait_random(max_delay=10):
    """waits for a random delay between 0 and max_delay"""

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
