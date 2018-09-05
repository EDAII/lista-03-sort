def make_heap(array, size_of_heap, index):
    largest = index
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    if left_child < size_of_heap and array[index] < array[left_child]:
        largest = left_child
    # See if right_child of root exists and is
    # greater than root
    if right_child < size_of_heap and array[largest] < array[right_child]:
        largest = right_child
    # Change root, if needed
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        make_heap(array, size_of_heap, largest)

def heapsort(array):
    size_of_heap = len(array)

    # Build a maxheap.
    for index in range(size_of_heap, -1, -1):
        make_heap(array, size_of_heap, index)

    # extract elements
    for index in range(size_of_heap-1, 0, -1):
        array[index], array[0] = array[0], array[index]
        make_heap(array, index, 0)

# test the algorithm

array = [ 12, 11, 13, 5, 6, 7]

heapsort(array)

size_of_heap = len(array)

print ("Sorted array is")

for index in range(size_of_heap):
    print("%d" %array[index])
