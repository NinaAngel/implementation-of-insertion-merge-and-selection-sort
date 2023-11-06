import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [56, 98, 45, 33, 2, 15, 48, 99, 100, 4, 5, 17, 28, 64, 13, 18, 27, 47, 19]


start_time = time.time()


selection_sort(arr)


end_time = time.time()


elapsed_time = end_time - start_time


print("Sorted Array:", arr)
print(f"Time taken to sort the array: {elapsed_time:.6f} seconds")
