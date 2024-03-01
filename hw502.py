def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return iterations, arr[left] if left < len(arr) else None

# Example usage:
sorted_array = [0.1, 0.5, 1.2, 1.8, 2.5, 3.7, 4.9]
target = 1.6
iterations, upper_bound = binary_search(sorted_array, target)
print(f"Iterations: {iterations}, Upper Bound: {upper_bound}")
