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