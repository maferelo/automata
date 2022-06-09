import random
import time
from queue import Queue  # Thread safe, process safe
from threading import Lock, Thread, current_thread

database_value = 0


def increase(lock, q):
    global database_value
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(1)
        database_value = local_copy
    print(f"end increase / q == {list(q.queue)} / {current_thread().name}")
    time.sleep(random.randint(1, 5))
    q.put(1)
    q.task_done()


def main():
    global database_value
    threads = []
    q = Queue()  # FIFO
    num_threads = 10
    lock = Lock()

    # create threads
    for _ in range(num_threads):
        thread = Thread(target=increase, args=(lock, q))
        thread.daemon = True
        threads.append(thread)

    # start threads
    for thread in threads:
        thread.start()

    # join th reads : wait for them to complete
    for thread in threads:
        thread.join()

    q.join()

    print("end main")


if __name__ == "__main__":
    main()
