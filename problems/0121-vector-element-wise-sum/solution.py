def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
    # Return the element-wise sum of vectors 'a' and 'b'.
    if len(a)!= len(b):
        return -1
    result = []
    for k in range(len(a)):
        result.append(a[k]+b[k])
    return result