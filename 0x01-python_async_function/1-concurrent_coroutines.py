#!/usr/bin/env python3
"""Contains a method that spawns wait_random n times with a
specified delay between each call."""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Calling wait_random n times
        with the specified max_delay
        return all the delayes appended to a list"""
    counter = 0
    all_delays = []

    while counter < n:
        random_delay = await wait_random(max_delay)
        all_delays.append(random_delay)
        counter += 1
    return all_delays
