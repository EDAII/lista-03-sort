def countingsort(array, digit):
    number = len(array)
    # The output array elements that will have sorted array
    output = [0] * (number)
    # initialize count array as 0
    count = [0] * (10)
    # Store count of occurrences in count[]
    for i in range(0, number):
        index = (array[i] / digit)
        count[int((index) % 10)] += 1
    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Build the output array
    i = number - 1
    while i >= 0:
        index = (array[i] / digit)
        output[count[ int((index) % 10)] - 1] = array[i]
        count[ int((index) % 10) ] -= 1
        i -= 1
    # Copying the output array to array[],
    # so that array now contains sorted numbers
    i = 0
    for i in range(0, len(array)):
        array[i] = output[i]

