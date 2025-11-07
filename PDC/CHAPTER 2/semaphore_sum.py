import threading
import time

data = list(range(1, 1_000_001))  # 1 million numbers
total_sum = 0
semaphore = threading.Semaphore(2)  # allows 2 threads to access the critical section at once


def worker(numbers):
    global total_sum
    partial = sum(numbers)
    with semaphore:  # only 2 threads can enter this block at once
        temp = total_sum
        time.sleep(0.001)  # simulate processing delay
        total_sum = temp + partial


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
    print(f"Semaphore sum: {total_sum}, Time taken: {end - start:.5f} sec")


if __name__ == "__main__":
    main()
