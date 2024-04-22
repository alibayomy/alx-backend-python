#!/usr/bin/env python3
"""Contains a method that measure the total execution time of
a function"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay),
        and returns total_time / n. Your function should return a float"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapsed_time = start_time - end_time
    return elapsed_time / n