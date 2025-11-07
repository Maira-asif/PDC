from multiprocessing import Process
import time

def worker():
    print("Worker started...")
    time.sleep(3)
    print("Worker finished.")

if __name__ == "__main__":
    p = Process(target=worker)
    p.daemon = False  # Daemon off (waits for child to finish)
    p.start()
    print("Main process waiting for worker...")
    p.join()
    print("All processes done.")
