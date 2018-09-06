from counting import countingsort

def radixsort(array):
    max_number = max(array)
    exp_digit = 1
    while max_number / exp_digit > 0:
        countingsort(array, exp_digit)
        exp_digit *= 10
