#algorithms
from heap import heapsort
from heap import make_heap
from merge import mergesort
from merge import mergesort_time
from quick import quicksort
from counting import countingsort
from radix import radixsort
from shell import shellsort

#utils
from populate import populate
import time 


v100 = list(range(0,100))
v1000 = list(range(0,1000))
v10000 = list(range(0,10000))

v100 = populate(v100)
v1000 = populate(v1000)
v10000 = populate(v10000)


def time_execute_shellsort_v100():

	before = time.time()
	shellsort(v100)
	after = time.time()
	total = ((after-before)*1000)

	print("time shellsort (100 elements) = %0.4f" % total)


time_execute_shellsort_v100()

def time_execute_shellsort_v1000():

	before = time.time()
	shellsort(v1000)
	after = time.time()
	total = ((after-before)*1000)

	print("time shellsort (1000 elements) = %0.4f" % total)


time_execute_shellsort_v1000()

def time_execute_shellsort_v10000():

	before = time.time()
	shellsort(v10000)
	after = time.time()
	total = ((after-before)*1000)

	print("time shellsort = (10000 elements) %0.4f" % total)


time_execute_shellsort_v10000()

def time_execute_quicksort_v100():
	before = time.time()
	quicksort(v100)
	after = time.time()
	total = ((after-before)*1000)

	print("time quicksort = (100 elements) %0.4f" %total)

time_execute_quicksort_v100()


def time_execute_quicksort_v1000():
	before = time.time()
	quicksort(v1000)
	after = time.time()
	total = ((after-before)*1000)

	print("time quicksort = (1000 elements) %0.4f" %total)

time_execute_quicksort_v1000()


def time_execute_quicksort_v10000():
	before = time.time()
	quicksort(v10000)
	after = time.time()
	total = ((after-before)*1000)

	print("time quicksort = (10000 elements) %0.4f" %total)

time_execute_quicksort_v10000()

def time_execute_heapsort_v100():
	before = time.time()
	heapsort(v100)
	after = time.time()
	total = ((after-before)*1000)

	print("time heapsort = (100 elements) %0.4f" %total)

time_execute_heapsort_v100()

def time_execute_heapsort_v1000():
	before = time.time()
	heapsort(v1000)
	after = time.time()
	total = ((after-before)*1000)

	print("time heapsort = (1000 elements) %0.4f" %total)

time_execute_heapsort_v1000()


def time_execute_heapsort_v10000():
	before = time.time()
	heapsort(v10000)
	after = time.time()
	total = ((after-before)*1000)

	print("time heapsort = (10000 elements) %0.4f" %total)

time_execute_heapsort_v10000()



