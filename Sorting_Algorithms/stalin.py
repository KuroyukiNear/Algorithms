import time

# Initial list to be sorted
sortme = [13, 35, 17, 42, 21, 3, 30, 25, 4, 49, 16, 27, 2, 31, 12, 37, 23, 36, 19, 40, 22, 48, 33, 34, 6, 10, 1, 14, 32, 29, 50, 24, 38, 7, 5, 44, 28, 26, 20, 41, 9, 43, 11, 8, 45, 15, 18, 47, 46, 39]

# Attempt Counter
attempts = 0

def attempt():
    global attempts
    attempts += 1

# Sort Checker
def is_sorted(arr):
    # Check if the array is sorted in ascending order.
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Sorting Algorithm
def search_n_exterminate(arr):
    i = 0
    changed = False
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            del arr[i]
            changed = True
        else:
            i += 1
    return changed

def main(tobe_sort):
    start_time = time.time()
    while True:
        attempt()
        if not search_n_exterminate(tobe_sort):
            break
        print(tobe_sort)
    elapsed_time = time.time() - start_time
    print(f"{attempts} attempts in {elapsed_time:.6f} seconds")
    print("Complete.")
    print(tobe_sort)

if __name__ == "__main__":
    main(sortme)
