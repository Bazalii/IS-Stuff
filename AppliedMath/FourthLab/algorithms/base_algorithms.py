import scipy.sparse


def generate_empty_matrix(n, m, input_format):
    matrix = scipy.sparse.__dict__[input_format + "_matrix"]
    return matrix((n, m))


def generate_identity_matrix(n, input_format):
    return scipy.sparse.identity(n, format=input_format)


def generate_hilbert_matrix(k):
    matrix = generate_empty_matrix(k, k, "lil")
    for i in range(k):
        for j in range(k):
            matrix[i, j] = 1.0 / (i + j + 1.0)

    return matrix.tocsr()


def generate_diagonal_domination_matrix(a, k):
    n = len(a)
    
    matrix = generate_empty_matrix(n, n, "lil")

    for i in range(n):
        t1 = -sum(a[i][k] for k in range(i))
        t2 = -sum(a[i][k] for k in range(i + 1, n))
        t = t1 + t2
        for j in range(n):
            if i != j:
                matrix[i, j] = a[i, j]
            else:
                matrix[i, j] = t + pow(10.0, -k)

    matrix = matrix.tocsr()
    return matrix
