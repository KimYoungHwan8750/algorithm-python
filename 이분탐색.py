list_ = [1, 10, 33, 18, 22, 90, 111, 9999, 837]


def binary_search(arr, start, end, target):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
    return binary_search(arr, start, end, target)

list_.sort()
print(binary_search(list_, 0, len(list_)-1, 9999))