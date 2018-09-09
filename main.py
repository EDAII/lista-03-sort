# algorithms
from heap import heapsort
from heap import make_heap
from merge import mergesort
from quick import quicksort
from quick import quicksort_graph
from counting import countingsort
from radix import radixsort
from shell import shellsort
from insertion import insertion_sort
from bucketsort import bucketsort
# utils
from populate import populate
import time
import random

# import the chart lib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

DEFAULT_BUCKET_SIZE = 5

v100 = list(range(0,100))
v1000 = list(range(0,1000))
v10000 = list(range(0,10000))

v100 = populate(v100)
v1000 = populate(v1000)
v10000 = populate(v10000)



if __name__ == "__main__":

	number_interation = int(input("Digite o numero de inteiros: "))

	input_message = "Selecione o metodo que deseja executar\n(i)nsertion sort\n(b)ucket sort\n(m)erge sort\n(s)hell sort\n(q)uick sort"
	input_is = input(input_message)
	
	# Build and randomly shuffle list of integers.
	vector = [x + 1 for x in range(number_interation)]
	random.seed(time.time())
	random.shuffle(vector)

	if input_is == "i":
		title = "Insertion Sort"
		generator = insertion_sort(vector)
	elif input_is == "b":
		title = "Bucket Sort"
		generator = bucketsort(vector,bucketSize=DEFAULT_BUCKET_SIZE)
	elif input_is == "m":
		title = "Merge Sort"
		generator = mergesort(vector,0,number_interation-1)
	elif input_is == "s":
		title = "Shell Sort"
		generator = shellsort(vector)
	elif input_is == "q":
		title = "Quick Sort"
		generator = quicksort_graph(vector,0,number_interation-1)

	# Inicializando grafico
	fig, ax = plt.subplots()
	ax.set_title(title)

	#bar

	bar = ax.bar(range(len(vector)), vector, align="edge")

	ax.set_xlim(0,number_interation)
	ax.set_ylim(0, int(1.07* number_interation))

	text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
	text_time = ax.text(0.02, 0.75, "", transform=ax.transAxes)

	start_time = time.time()
	iteration = [0]
	def update_fig(vector, rects, iteration):
	    for rect, val in zip(rects, vector):
	        rect.set_height(val)
	    iteration[0] += 1
	    text.set_text("# of operations: {}".format(iteration[0]))

	text_time.set_text("time: {}".format((time.time() - start_time)*1000))


	anim = animation.FuncAnimation(fig, func=update_fig,
	    fargs=(bar, iteration), frames=generator, interval=1,
	    repeat=False)
	plt.show()
