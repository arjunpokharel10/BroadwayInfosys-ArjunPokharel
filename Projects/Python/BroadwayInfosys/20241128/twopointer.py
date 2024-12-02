def sum_pair(arr, target):
    low, high = 0, len(arr) - 1

    while low < high:
        current_sum = arr[low] + arr[high]

        if current_sum == target:
            return (arr[low], arr[high])
        elif current_sum > target:
            high -= 1
        else:
            low += 1

    return None


arr = [1, 4, 6, 8, 13, 15, 66, 67, 87, 99]
target = 133

print(sum_pair(arr, target))