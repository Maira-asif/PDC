import threading
import time

data = list(range(1, 1_000_001))  # 1 million numbers
total_sum = 0
rlock = threading.RLock()  # Re-entrant Lock


def worker(numbers):
    global total_sum
    partial = sum(numbers)
    with rlock:  # same as Lock but allows the same thread to acquire it multiple times
        total_sum += partial


def main():
    global total_sum
    start = time.time()

    # Split data into 4 chunks for threads
    chunk_size = len(data) // 4
    threads = []

    for i in range(4):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size
        t = threading.Thread(target=worker, args=(data[start_index:end_index],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f"RLock sum: {total_sum}, Time taken: {end - start:.5f} sec")


if __name__ == "__main__":
    main()
