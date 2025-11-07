from threading import Barrier, Thread
import time

def worker(barrier, name):
    print(f"{name} working...")
    time.sleep(1)
    print(f"{name} waiting at barrier")
    barrier.wait()
    print(f"{name} passed the barrier")

if __name__ == "__main__":
    barrier = Barrier(3)
    threads = [Thread(target=worker, args=(barrier, f"Thread-{i+1}")) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
