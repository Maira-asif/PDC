from multiprocessing import Process
import time
import os

def worker():
    print(f"Started process {os.getpid()}")
    time.sleep(5)
    print("This line will not run if process is killed.")

if __name__ == "__main__":
    p = Process(target=worker)
    p.start()
    time.sleep(2)
    print("Main process killing child process...")
    p.terminate()  # Kill the process
    p.join()
    print("Process killed successfully.")
