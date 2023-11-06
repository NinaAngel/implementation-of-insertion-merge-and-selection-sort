import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [56, 98, 45, 33, 2, 15, 48, 99, 100, 4, 5, 17, 28, 64, 13, 18, 27, 47, 19]

start_time = time.time()
insertion_sort(arr)
end_time = time.time()
execution_time = end_time - start_time

print("Sorted array:", arr)
print("Time taken: {:.6f} seconds".format(execution_time))
