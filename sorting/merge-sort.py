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


# Assume 4 operation per iterations in the main for loop (k): comparison, append
# and increase k and i or j. So running time of merge on array of m number is
# <= 4m+2 (upshot) -- without considering recursion.
# Note: this assumption is fine even if we might argue there are more than 4
# ops. It doesn't really matter in the end (it's a constant).
# We can further simplify operations by saying 4m+2 <= 6m, since m>=1.

# Considering recursion:
# Merge sort requires <=6n*log2(n)+6n ~O(n*log(n)) operations to sort n numbers.
# This is much faster than O(n^2) algorithms to sort arrays, and shows how
# powerful the divide and conquer approach is.

# Proof: https://www.youtube.com/watch?v=8ArtRiTkYEw
# Using recursion tree. Intuition (assuming n is a power of 2), the levels of
# the recursion tree are [outer, 1, 2, ..., log2(n)], so there are log2(n)+1
# levels of the recursion tree.
#
#  Level 0 (outer call)            o
#                                /   \
#  Level 1                      o     o
#                              / \   / \
#  Level 2                    o   o o   o
#
#                                ...
# 
#                      o       o       o       o
#                     / \     / \     / \     / \
#  Level log2(n)     o   o   o   o   o   o   o   o   ...  (base cases)
#
# The reason the last level is log2(n) is that the input size is being
# decreased by a factor of 2 at each level of the recursion. So the level 0
# (outer call) will operate on an array of size n, level 1 on an array of
# size n/2, level 3 on size n/4, ..., level log2(n) on size <=1. 
#
# Note that at each level j=0,1,2,...,log2(n), there are 2^j subproblems
# (the number of subproblems doubles at each level), each of size n/2^j
# (the size of the array halves at each level).
#
# To calculate the "work" per level, we can consider the work required at
# each level of the tree (do not consider recursive calls of the level).
#    2^j (#level-j subproblems) + 6*(n/2^j) (array size at level j) =
#  = 6n <- The 2^j factor cancels out!
#
# Since there are log2(n)+1 levels, we get that merge sort requires
#   <= 6n*(log2(n)+1)=6n*log2(n)+6n  ~O(n*log2(n))
# operations, as stated previously.