#!/usr/bin/env python3
import asyncio
import time

async def sleep():
    print('Hello')
    await asyncio.sleep(3)
    print('World')

async def main():
    tasks = []
    for _ in range(3):
        task = asyncio.ensure_future(sleep())
        tasks.append(task)
    await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    
    
    start_time = time.time()
    # asyncio.run(main())
    asyncio.get_event_loop().run_until_complete(main())
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
