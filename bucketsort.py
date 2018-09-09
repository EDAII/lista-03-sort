import math
from insertion import insertion_sort

DEFAULT_BUCKET_SIZE = 5

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

	bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
	# 81 - 6 = 75/5 = 15 + 1 = [16]

	#initialize buckets
	buckets = []
	for i in range(0,bucketCount):
		buckets.append([])

	#put the values in bucketsort

	for i in range(0,len(vector)):
		buckets[math.floor((vector[i] - minValue) / bucketSize)].append(vector[i])
		#append the value 22 on buckets[3]
		# append the value 45 on bucket[7]
		#append the value 12 on bucket [1]

	#sorted buckets and place back

	new_vector = []
	for i in range(0,len(buckets)):
		insertion_sort(buckets[i])
		for j in range(0,len(buckets[i])):
			new_vector.append(buckets[i][j])

	yield new_vector
