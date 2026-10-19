def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	n=len(b)

	if len(a)!=n:
		return-1

	result=[]
	
	for L in a:
		sum=0
		for k in range(n):
			sum+=L[k]*b[k]
		result.append(sum)

	return result
	
	pass