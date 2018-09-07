def shellsort(vector):

	length = len(vector)
	gap = int(length/2)

	while(gap>=1):
		i=gap
		while(i<length):
			value = vector[i]
			j=i
			while(j - gap >=0 and value < vector[j-gap]):
				vector[j] = vector[j-gap]
				j-=gap
			vector[j] = value
			i+=1
		gap = int(gap/2)
