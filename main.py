# algorithms
from heap import heapsort
from heap import make_heap
from merge import mergesort
from quick import quicksort
from counting import countingsort
from radix import radixsort
from shell import shellsort
# utils
from populate import populate
import time

#time functions 
from time_execute import time_execute_shellsortv100
from time_execute import time_execute_shellsortv1000
from time_execute import time_execute_shellsortv10000
# import the chart lib


v100 = list(range(0,100))
v1000 = list(range(0,1000))
v10000 = list(range(0,10000))

v100 = populate(v100)
v1000 = populate(v1000)
v10000 = populate(v10000)

