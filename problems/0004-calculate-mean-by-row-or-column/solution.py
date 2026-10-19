def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	def transpose_matrix(a):
		n,m=len(a),len(a[0])
		b=[[0 for _ in range(n)] for _ in range(m)]
		for i in range(n):
			for j in range(m):
				b[j][i]=a[i][j]
		return b

	if mode=="row":
		means=[]
		for L in matrix:
			sum=0
			for k in L:
				sum+=k
			means.append(sum/len(L))
		return means
	
	else:
		return calculate_matrix_mean(transpose_matrix(matrix),"row")

	