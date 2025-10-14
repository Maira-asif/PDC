import threading
import time

data = list(range(1, 1_000_001))  # 1 million numbers
total_sum = 0
condition = threading.Condition()
done_threads = 0
total_threads = 4  # we’ll use 4 threads


def worker(numbers):
    global total_sum, done_threads
    partial = sum(numbers)

    with condition:
        # Wait if another thread is currently updating
        condition.wait_for(lambda: done_threads == 0)

        temp = total_sum
        time.sleep(0.001)  # simulate processing delay
        total_sum = temp + partial
        done_threads += 1

        # Notify next thread when finished
        condition.notify_all()


def main():
    global total_sum, done_threads
    start = time.time()

    chunk_size = len(data) // total_threads
    threads = []

    for i in range(total_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size
        t = threading.Thread(target=worker, args=(data[start_index:end_index],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f"Condition sum: {total_sum}, Time taken: {end - start:.5f} sec")


if __name__ == "__main__":
    main()

