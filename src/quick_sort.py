from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    def _quick_sort(arr, low, high):
        if low < high:
            pi = _partition(arr, low, high)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)

    def _partition(arr, low, high):
        pivot = arr.get(high)
        i = low - 1
        for j in range(low, high):
            if arr.get(j) <= pivot:
                i += 1
                temp = arr.get(i)
                arr.set(i, arr.get(j))
                arr.set(j, temp)
        temp = arr.get(i + 1)
        arr.set(i + 1, arr.get(high))
        arr.set(high, temp)
        return i + 1

    if len(array) > 0:
        _quick_sort(array, 0, len(array) - 1)
    return array
