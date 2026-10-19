def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	(a,b),(c,d)=matrix[0],matrix[1]
	trace=a+d
	det=a*d-b*c
	det_quad=trace**2-4*det
	eigenvalues=[trace/2+(det_quad/4)**0.5,trace/2-(det_quad/4)**0.5]
	return eigenvalues