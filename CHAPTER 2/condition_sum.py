import threading
import time

# Shared variables
data = list(range(1, 1_000_001))  # 1 to 1 million
total_sum = 0
done_threads = 0
total_threads = 4  # number of worker threads

# Create a Condition object
condition = threading.Condition()

def worker(numbers):
    global total_sum, done_threads

    # Calculate partial sum
    part_sum = sum(numbers)

    # Synchronize access to shared variables
    with condition:
        total_sum += part_sum
        done_threads += 1
        print(f"[{threading.current_thread().name}] done partial sum: {part_sum}")

        # Notify main thread if all are done
        if done_threads == total_threads:
            condition.notify_all()

def main():
    global total_sum, done_threads
    start = time.time()

    # Split data into equal parts
    chunk_size = len(data) // total_threads
    threads = []

    for i in range(total_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size
        t = threading.Thread(
            target=worker,
            args=(data[start_index:end_index],),
            name=f"Thread-{i+1}"
        )
        threads.append(t)
        t.start()

    # Wait until all threads finish
    with condition:
        while done_threads < total_threads:
            condition.wait()

    end = time.time()
    print(f"\nTotal sum: {total_sum}")
    print(f"Time taken: {end - start:.5f} seconds")

if __name__ == "__main__":
    main()


