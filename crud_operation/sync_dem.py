import time 
from timeit import default_timer as timer



def run_task(name,seconds):
    print(f"{name}started as :{timer()}")
    time.sleep(seconds)
    print(f"{name}ended as :{timer()}")

start=timer()
run_task("task1",2)
run_task("task2",1)
run_task("task3",3)
print(f"total time taken :{timer()-start} seconds")