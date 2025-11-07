from multiprocessing import Pool
import time

def square(n):
    time.sleep(0.5)
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    with Pool(processes=3) as pool:
        results = pool.map(square, numbers)
    print(f"Squares: {results}")
