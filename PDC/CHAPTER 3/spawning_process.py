from multiprocessing import get_context
import time

def show_process(n):
    print(f"Running task {n}")
    time.sleep(1)

if __name__ == "__main__":
    ctx = get_context("spawn")  # 'spawn' start method
    processes = [ctx.Process(target=show_process, args=(i,)) for i in range(3)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print("All spawned processes done.")
