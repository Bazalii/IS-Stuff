import numpy as np
import scipy.sparse


def generate_empty_matrix(n, m, format):
    matrix = scipy.sparse.__dict__[format + "_matrix"]
    return matrix((n, m))


def generate_identity_matrix(n, format):
    return scipy.sparse.identity(n, format=format)


def generate_ascending_vector(n):
    return np.array(list(range(1, n + 1)))


def generate_big_matrix(n, p, format):
    return scipy.sparse.random(n, n, p, format=format)


def generate_random_vector(n):
    return generate_ascending_vector(n)


def generate_hilbert_matrix(k):
    A_k = generate_empty_matrix(k, k, "lil")
    for i in range(k):
        for j in range(k):
            A_k[i, j] = 1.0 / (i + j + 1.0)

    return A_k.tocsr()


def generate_diagonal_domination_matrix(a, k):
    n = len(a)
    A_k = generate_empty_matrix(n, n, "lil")

    for i in range(n):
        t1 = -sum(a[i][k] for k in range(i))
        t2 = -sum(a[i][k] for k in range(i + 1, n))
        t = t1 + t2
        for j in range(n):
            if i != j:
                A_k[i, j] = a[i, j]
            else:
                A_k[i, j] = t + pow(10.0, -k)

    A_k = A_k.tocsr()
    return A_k
