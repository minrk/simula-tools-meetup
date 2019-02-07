#!/usr/bin/env python3
import asyncio
import time


async def cpu_bound(number):
    return sum(i * i for i in range(number))


async def find_sums(numbers):
    tasks = []
    for number in numbers:
        task = asyncio.ensure_future(cpu_bound(number))
        tasks.append(task)
    await asyncio.gather(*tasks, return_exceptions=True)



if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    # asyncio.run(find_sums(numbers))
    asyncio.get_event_loop().run_until_complete(find_sums(numbers))
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")


    
