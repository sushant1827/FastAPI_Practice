import asyncio
from timeit import default_timer as timer

async def run_task(name, seconds):
    print(f'{name} started at {timer()}')
    await asyncio.sleep(seconds)
    print(f'{name} ended at {timer()}')

async def main():
    start_time = timer()
    await asyncio.gather(
        run_task('Task 1', 2),
        run_task('Task 2', 3),
        run_task('Task 2', 5)
    )
    print(f'Total time taken: {timer() - start_time:.2f} seconds')

asyncio.run(main())