import os
import random
import time
from multiprocessing import Array, Lock, Pool, Process, Queue, Value


def square_numbers(shared_number, lock):
    for _ in range(100):
        time.sleep(random.randint(1, 5) / 100)
        with lock:
            shared_number.value += 1


def cube(n):
    return n * n * n


def main():
    processes = []
    num_processes = os.cpu_count()
    shared_number = Value("i", 0)
    lock = Lock()

    for _ in range(num_processes):
        process = Process(target=square_numbers(shared_number, lock))
        processes.append(process)

    for process in processes:
        process.start()

    # wait for all processes to tinish
    # block the main programm until these processes are finished
    for process in processes:
        process.join()

    print(shared_number.value)

    # map, apply, join and close
    pool = Pool()
    # creates processes according to the number of cores
    # split iterable into chunks of size n processes
    result = pool.map(cube, range(1, 11))
    # pool.spply(cube, 1)
    pool.close()
    pool.join()
    print(result)


if __name__ == "__main__":
    main()
