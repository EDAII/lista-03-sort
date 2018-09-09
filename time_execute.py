#algorithms
from heap import heapsort
from heap import make_heap
from merge import mergesort
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
	total = ((after-before)*100)

	print("time shellsort (100 elements) = %0.2f" % total)


time_execute_shellsort_v100()

def time_execute_shellsort_v1000():

	before = time.time()
	shellsort(v1000)
	after = time.time()
	total = ((after-before)*100)

	print("time shellsort (1000 elements) = %0.2f" % total)


time_execute_shellsort_v1000()

def time_execute_shellsort_v10000():

	before = time.time()
	shellsort(v10000)
	after = time.time()
	total = ((after-before)*100)

	print("time shellsort = (10000 elements) %0.2f" % total)


time_execute_shellsort_v10000()

def time_execute_mergesort_v100():
	before = time.time()
	mergesort(v100,0,v100-1)
	after = time.time()
	total = ((after-before)*100)

	print("time mergesort = (100 elements) %0.2f" %total)

time_execute_mergesort_v100()


def time_execute_mergesort_v1000():
	before = time.time()
	mergesort(v1000,0,v100-1)
	after = time.time()
	total = ((after-before)*100)

	print("time mergesort = (1000 elements) %0.2f" %total)

time_execute_mergesort_v1000()


def time_execute_mergesort_v10000():
	before = time.time()
	mergesort(v10000,0,v100-1)
	after = time.time()
	total = ((after-before)*100)

	print("time mergesort = (10000 elements) %0.2f" %total)

time_execute_mergesort_v10000()



