def insertion_sort(a):
    for i in range(1, len(a)):  # skip first element (already sorted)
        for j in reversed(range(1, i+1)):  # j = i, i-1, ..., 1
            if a[j-1] > a[j]:  # j-1 includes the check for index 0
                a[j-1], a[j] = a[j], a[j-1]
                
    return a


print(insertion_sort([4, 1, 3, 3, 2, 2, 2]))
print(insertion_sort([2, 6, 4, 1, 3, 8, 9, 0, 7, 5]))


# Time complexity: quadratic O(n^2)
# In the worst case (i.e., array sorted in reverse order), each iteration will
# scan the array until the i-th element and place the current element at index i.

# Space complexity: constant O(1)


# Alternate version using list.pop and list.insert
def insertion_sort_popinsert(a):
    for i in range(1, len(a)):  # skip first element (already sorted)
        cur = a.pop(i)  # O(n)
        
        for j in range(i+1):
            if j == i or a[j] > cur:  # must use short-circuit evaluation
                a.insert(j, cur)  # O(n)
                break
                
    return a


print(insertion_sort_popinsert([4, 1, 3, 3, 2, 2, 2]))
print(insertion_sort_popinsert([2, 6, 4, 1, 3, 8, 9, 0, 7, 5]))