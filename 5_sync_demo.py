import time
from timeit import default_timer as timer

def run_task(name, seconds):
    print(f'{name} started at {timer()}')
    time.sleep(seconds)
    print(f'{name} ended at {timer()}')

start_time = timer()

run_task('Task 1', 2)
run_task('Task 2', 3)
run_task('Task 2', 5)

print(f'Total time taken: {timer() - start_time} seconds')