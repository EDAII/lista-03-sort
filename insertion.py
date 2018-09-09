def insertion_sort(vector):
	i = 1
	# i go to end of the vector
	while i < len(vector):
		temporaria = vector[i]
		swap = False
		j = i - 1 #element to compair
		while j >= 0 and vector[j] > temporaria:
			vector[j+1] = vector[j]
			swap = True #swap
			j = j - 1
		if swap:
			vector[j+1] = temporaria
		i = i + 1

		yield vector

