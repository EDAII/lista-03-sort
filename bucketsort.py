import math

DEFAULT_BUCKET_SIZE = 10
vector = [22,45,12,8,10,6,72,81,33,18,50,14]

def bucketsort(vector, bucketSize=DEFAULT_BUCKET_SIZE):
	
	# se o tamanho do vetor for igual a = 0 ele ja esta ordenado
	if len(vector) == 0:
		return vector

	# Determinar o minimo e o valor máximo
	minValue = vector[0]
	maxValue = vector[0]

	for i in range (1, len(vector)):
		if vector[i] < minValue:
			minValue = vector[i]
		elif vector[i] > maxValue:
			maxValue = vector[i]

	# find a divider which will be used to put the elements in the buckets
	# ceil taken next max integer value
	divider = math.ceil((maxValue + 1)/bucketSize)

	# initialize buckets
	buckets = []

	for i in range(0,len(vector)):
		for j in range(0,len(vector)):
			j = floor(vector[i]/divider)
			buckets[j] = vector[i]

