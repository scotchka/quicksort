def qsort(array):
    _qsort(array, 0, len(array) - 1)


def _qsort(array, start, end):
    if end - start < 1:
        return
    else:
        pivot = partition(array, start, end)
        _qsort(array, start, pivot - 1)
        _qsort(array, pivot + 1, end)


def partition(array, start, end):
    # print array
    pivot = start  # pivot position to swap with pivot value; first value to the right
    for i in range(start, end):  # iterate from start to end - 1
        if array[i] <= array[end]:  # current value <= pivot value
            array[i], array[pivot] = array[pivot], array[i]  # swap current and value at pivot position
            pivot += 1  # update pivot position
            # print array
    array[end], array[pivot] = array[pivot], array[end]  # swap pivot value and value at pivot position
    # print array
    return pivot
