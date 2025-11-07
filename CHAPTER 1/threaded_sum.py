import threading
import time

def threaded_process(numbers, num_threads):
    start = time.time()
    chunk_size = len(numbers) // num_threads
    partial_sums = [0] * num_threads
    threads = []

    def worker(index, data):
        partial_sums[index] = sum(data)

    for i in range(num_threads):
        start_idx = i * chunk_size
        end_idx = len(numbers) if i == num_threads - 1 else (i + 1) * chunk_size
        t = threading.Thread(target=worker, args=(i, numbers[start_idx:end_idx]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total = sum(partial_sums)
    end = time.time()
    print(f"Threaded sum ({num_threads} threads): {total}, Time taken: {end - start:.5f} sec")

if __name__ == "__main__":
    data = list(range(1, 1_000_001))
    for n in [5, 10, 15, 50]:
        threaded_process(data, n)
