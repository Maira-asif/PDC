from multiprocessing import Process
import time

def background_task():
    while True:
        print("Background process running...")
        time.sleep(2)

if __name__ == "__main__":
    p = Process(target=background_task)
    p.daemon = True  # Runs in background
    p.start()
    print("Main process doing other work...")
    time.sleep(5)
    print("Main process done, background process will stop automatically.")
