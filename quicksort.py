def qsort(array):
    _qsort(array, 0, len(array) - 1)


def _qsort(array, start, end):
    if end - start < 1:
        return
    else:
        pivot = partition_hoare(array, start, end)
        _qsort(array, start, pivot - 1)
        _qsort(array, pivot + 1, end)


def partition_lomuto(array, start, end):
    pivot = start  # pivot position to swap with pivot value; first value to the right

    for i in range(start, end):  # iterate from start to end - 1
        if array[i] <= array[end]:  # current value <= pivot value
            array[i], array[pivot] = array[pivot], array[i]  # swap current and value at pivot position
            pivot += 1  # update pivot position

    array[end], array[pivot] = array[pivot], array[end]  # swap pivot value and value at pivot position
    return pivot


def partition_hoare(array, start, end):
    i, j = start, end - 1

    while True:
        while array[i] <= array[end] and i < j:
            i += 1

        while array[j] >= array[end] and i < j:
            j -= 1

        if i == j:
            if array[i] <= array[end]:
                i += 1

            array[i], array[end] = array[end], array[i]
            return i
        else:
            array[i], array[j] = array[j], array[i]

if __name__ == '__main__':
    import numpy as np
    from random import shuffle
    print 'test with random list of integers and floats...'
    test = list(np.random.randint(-50, 50, 500)) + list(np.random.uniform(-50, 50, 500))
    shuffle(test)
    control = sorted(test)
    qsort(test)
    print 'control == test:', control == test
