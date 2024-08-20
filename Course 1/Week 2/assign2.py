def merge_and_count_inversions(arr, temp, left, mid, right):
    """Merges two sorted subarrays and counts inversions."""
    inversions = 0
    i, j, k = left, mid, left  # i: left, j: right, k: temp

    while i < mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:  # Inversion found (arr[i] > arr[j])
            temp[k] = arr[j]
            j += 1
            inversions += mid - i  # Count inversions
        k += 1

    # Copy remaining elements (if any)
    temp[k:right+1] = arr[i:mid] + arr[j:right+1]
    arr[left:right+1] = temp[left:right+1]  
    return inversions

def count_inversions(arr, temp, left, right):
    """Recursively counts inversions in the array."""
    if right <= left:
        return 0  
    mid = (left + right) // 2
    left_inversions = count_inversions(arr, temp, left, mid)
    right_inversions = count_inversions(arr, temp, mid + 1, right)
    merge_inversions = merge_and_count_inversions(arr, temp, left, mid + 1, right)
    return left_inversions + right_inversions + merge_inversions



with open("IntegerArray.txt") as file:
   arr = [int(line.strip()) for line in file]


arr_size = len(arr)
temp = [0] * arr_size

inversion_count = count_inversions(arr, temp, 0, arr_size - 1)
print(f"Number of inversions: {inversion_count}")
