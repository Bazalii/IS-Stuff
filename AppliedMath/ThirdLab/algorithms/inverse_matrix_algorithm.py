from algorithms.slau_solution import get_system_solution
from algorithms.base_algorithms import generate_empty_matrix, generate_identity_matrix


def get_system_solution_matrix(A, B):
    N = A.shape[0]
    X = generate_empty_matrix(N, N, "lil")
    for i in range(N):
        X[i] = get_system_solution(A, B.getcol(i).toarray())
    return X.tocsr().transpose()


def get_inverse_matrix(A):
    return get_system_solution_matrix(A, generate_identity_matrix(A.shape[0], "csr"))
