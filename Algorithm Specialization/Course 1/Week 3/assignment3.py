def swap(arr, a, b):
    """Swaps two elements in an array."""
    arr[a], arr[b] = arr[b], arr[a]

def find_median(arr, l, r):
    """Finds the median of three elements in an array."""
    n = r - l + 1
    if n % 2 == 0:
        pos = n // 2 - 1 + l
    else:
        pos = n // 2 + l
    a, b, c = arr[l], arr[pos], arr[r]
    maxi = max(a, b, c)
    mini = min(a, b, c)
    if a != maxi and a != mini:
        return l
    elif b != maxi and b != mini:
        return pos
    else:
        return r

def partition(arr, l, r, pivot_option):
    """Partitions the array around a chosen pivot."""
    if pivot_option == "first":
        pi = l
    elif pivot_option == "last":
        pi = r
    elif pivot_option == "median":
        pi = find_median(arr, l, r)
    else:
        raise ValueError("Invalid pivot option")

    if pi != l:
        swap(arr, l, pi)
    pivot = arr[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if arr[j] < pivot:
            swap(arr, i, j)
            i += 1
    swap(arr, l, i - 1)
    return i - 1

def quick_sort(arr, l, r, pivot_option="median"):
    """Recursive QuickSort function."""
    if r <= l:
        return 0

    position = partition(arr, l, r, pivot_option)
    left = quick_sort(arr, l, position - 1, pivot_option)
    right = quick_sort(arr, position + 1, r, pivot_option)
    return left + right + r - l


# Example Usage (replace with your data source)
with open("QuickSort.txt") as file:
    arr = [int(line.strip()) for line in file]
#choose pivot_option
comparisons = quick_sort(arr, 0, len(arr) - 1, pivot_option="median")
print("Comparisons:", comparisons)
