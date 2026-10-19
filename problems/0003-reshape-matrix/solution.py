import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	n,m,(c,d)=len(a),len(a[0]),new_shape
	if n*m!=c*d:
		return []
	reshaped_matrix=[[0 for _ in range(d)] for _ in range(c)]
	ligne=0
	mod=0
	for i in range(n):
		for j in range(m):
			if mod==d:
				mod=0
				ligne+=1
			reshaped_matrix[ligne][mod]=a[i][j]
			mod+=1
	return reshaped_matrix