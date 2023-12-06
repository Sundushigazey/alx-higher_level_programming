def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        result = []
        for j in i:
                result.append(j ** 2)
        new_matrix.append(result)
    return new_matrix
