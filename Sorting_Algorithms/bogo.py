# 11 July 2024
# N34R

'''
hic sunt dracones
'''

import random
import time

sortme = [13, 35, 17, 42, 21, 3, 30, 25, 4, 49, 16, 27, 2, 31, 12, 37, 23, 36, 19, 40, 22, 48, 33, 34, 6, 10, 1, 14, 32, 29, 50, 24, 38, 7, 5, 44, 28, 26, 20, 41, 9, 43, 11, 8, 45, 15, 18, 47, 46, 39]

# Attempt Counter
attempts = 0
def attempt():
    global attempts
    attempts = attempts + 1

# Sort Checker
def is_sorted(arr):
    # Check if the array is sorted in ascending order.
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Sorting Algorithm
def randomise_array(arr):
    # Shuffle the array randomly.
    random.shuffle(arr)
    attempt()
    print(arr)
    return arr

def main(tobe_sort):
    # Keep randomising the array until it is sorted.
    start_time = time.time()
    while True:
        randomise_array(tobe_sort)
        if is_sorted(tobe_sort):
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"{attempts} attempts in {elapsed_time:.6f} seconds")
            print("Complete.")
            break

if __name__ == "__main__":
    main(sortme)
