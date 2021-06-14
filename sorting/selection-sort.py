def selection_sort(a):
    if not a:
        return a

    for i in range(len(a)):
        j_min = i
        for j in range(i+1, len(a)):
            if a[j] < a[j_min]:
                j_min = j
        
        if j_min != i:
            tmp = a[i]
            a[i] = a[j_min]
            a[j_min] = tmp
    
    return a

print(selection_sort([6, 27, 1, 36, 75, 3, 2, 6, 32, 26, 52, 64, 11, 12, 252, 52, 53, 12]))
print(selection_sort([2, 6, 4, 1, 3, 8, 9, 0, 7, 5]))

# Time complexity: quadratic (O(n^2))
# None of the loops depend on the data in the array; selecting the minimum requires
# scanning n elements (n-1 comparisons), and then swapping it into the first position.
# Finding the next lowest element requires n-2 comparisons and so on.
# So we get n of comparisons (n-1) + (n-2) + ... 1 which is O(n^2) in complexity

# Space complexity: constant (O(1))