#!/usr/bin/env python3
"""Contains a method that spawns Tasks n times with a
specified delay between each call."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """Calling wait_random n times
        with the specified max_delay
        return all the delayes appended to a list"""
    counter = 0
    all_delays = []

    while counter < n:
        random_delay = await task_wait_random(max_delay)
        all_delays.append(random_delay)
        counter += 1
    return sorted(all_delays)
