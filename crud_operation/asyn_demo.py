import time 
import asyncio
from timeit import default_timer as timer

async def run_task(name,seconds):
    print(f"{name}started as :{timer()}")
    await asyncio.sleep(seconds)
    print(f"{name}ended as :{timer()}")

async def main():
    start = timer()
    await asyncio.gather(
        run_task("task1",2),
        run_task("task2",1),
        run_task("task3",3)
    )
    print(f"total time taken :{timer()-start} seconds")
asyncio.run(main())