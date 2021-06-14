# Divide and conquer approach
# Recursive algorithm

# Assume distinct numbers in input array


def merge_sort(arr):
    if len(arr) < 2:  # base case: 1 or 0 length is already sorted
        return arr

    i_split = len(arr) // 2
    arr1 = arr[:i_split]
    arr2 = arr[i_split:]

    arr1_sorted = merge_sort(arr1)
    arr2_sorted = merge_sort(arr2)
    arr_sorted = []
    
    i = 0
    j = 0
    for k in range(len(arr)):
        if arr1_sorted[i] < arr2_sorted[j]:
            arr_sorted.append(arr1_sorted[i])
            i += 1
            
            if i >= len(arr1_sorted):
                arr_sorted.extend(arr2_sorted[j:])
                return arr_sorted
        
        else:
            arr_sorted.append(arr2_sorted[j])
            j += 1
            
            if j >= len(arr2_sorted):
                arr_sorted.extend(arr1_sorted[i:])
                return arr_sorted


print(merge_sort([6, 27, 1, 36, 75, 3, 2, 6, 32, 26, 52, 64, 11, 12, 252, 52, 53, 12]))
print(merge_sort([2, 6, 4, 1, 3, 8, 9, 0, 7, 5]))
print(merge_sort([1]))
print(merge_sort([]))
print(merge_sort([100, 102, 101, 99, 103]))
