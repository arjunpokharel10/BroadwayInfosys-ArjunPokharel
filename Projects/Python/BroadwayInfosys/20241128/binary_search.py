def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid            
        elif arr[mid] < target:
            left = mid + 1
        else:
            arr[mid] > target
            right = mid - 1          
    return None
            



arr = [1, 5, 77, 99, 101, 114, 455, 750]
target = 99
print(binary_search(arr, target))