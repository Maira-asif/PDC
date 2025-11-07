from multiprocessing import Process, current_process
import time

def task():
    print(f"Running: {current_process().name}")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(3):
        p = Process(target=task, name=f"Worker-{i+1}")
        p.start()
        p.join()
