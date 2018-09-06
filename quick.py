def quicksort(array):
    # check if array has only one element and returns it
    if len(array) == 1 or len(array) == 0:
        return array
    else:
        pivot = array[0]
        i = 0
        for j in range(len(array)-1):
            if array[j + 1] < pivot:
                array[j + 1], array[i + 1] = array[i + 1], array[j + 1]
                i += 1

        array[0], array[i] = array[i], array[0]

        first_part = quicksort(array[:i])

        second_part = quicksort(array[i+1:])

        first_part.append(array[i])

        return first_part + second_part
