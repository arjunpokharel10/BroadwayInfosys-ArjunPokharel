# to sort an array using merge sort:
# - split it into two parts
# - sort the left part
# - sort the right part
# - join parts into a sorted array

def mergesortedarr(left, right):
    sorted_arr = []
    while left and right:
        if left[0] <= right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
    # Add any remaining elements
    sorted_arr.extend(left if left else right)
    return sorted_arr

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        left = mergesort(left)
        right = mergesort(right)
        return mergesortedarr(left,right)
    
print(mergesort([1, 2, 5, 4, 3, 7, 22, 65, 22, 21, 34, 41, 37, 29, 9, 20]))
