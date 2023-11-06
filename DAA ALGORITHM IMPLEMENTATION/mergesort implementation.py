import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_half) and right_idx < len(right_half):
        if left_half[left_idx] < right_half[right_idx]:
            result.append(left_half[left_idx])
            left_idx += 1
        else:
            result.append(right_half[right_idx])
            right_idx += 1

    result.extend(left_half[left_idx:])
    result.extend(right_half[right_idx:])

    return result


arr = [11, 25, 46, 98, 75, 12, 45, 69, 100, 75, 40, 19, 81]


start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()
elapsed_time = end_time - start_time

print("Sorted array:", sorted_arr)
print("Time taken:", elapsed_time, "seconds")
