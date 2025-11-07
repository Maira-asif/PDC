import time

def process(numbers):
    start = time.time()
    total = sum(numbers)
    end = time.time()
    print(f"Normal sum: {total}, Time taken: {end - start:.5f} sec")

if __name__ == "__main__":
    data = list(range(1, 1_000_001))  # 1 million numbers
    process(data)
