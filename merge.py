def mergesort(vector, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(vector, start, mid)
    yield from mergesort(vector, mid + 1, end)
    yield from merge(vector, start, mid, end)
    yield vector

def merge(vector, start, mid, end):
    """Helper function for merge sort."""
    
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if vector[leftIdx] < vector[rightIdx]:
            merged.append(vector[leftIdx])
            leftIdx += 1
        else:
            merged.append(vector[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(vector[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(vector[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        vector[start + i] = sorted_val
        yield vector

def mergesort_time(array):
    # split
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        mergesort_time(left)
        mergesort_time(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = right[j]
            j += 1
            k += 1