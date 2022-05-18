import numpy as np

from algorithms.base_algorithms import generate_empty_matrix, generate_identity_matrix


def get_lil_row_product(first_matrix, second_matrix, first_row_indexes, second_row_indexes):
    first_row = first_matrix.rows[first_row_indexes]
    second_row = second_matrix.rows[second_row_indexes]
    first_data = first_matrix.data[first_row_indexes]
    second_data = second_matrix.data[second_row_indexes]

    result = 0

    first_matrix_counter = 0
    second_matrix_counter = 0

    while first_matrix_counter < len(first_row) and second_matrix_counter < len(second_row):
        first_indexes_position = first_row[first_matrix_counter]
        second_indexes_position = second_row[second_matrix_counter]

        if first_indexes_position == second_indexes_position:
            result += first_data[first_matrix_counter] * second_data[second_matrix_counter]
            first_matrix_counter += 1
        elif first_indexes_position < second_indexes_position:
            first_matrix_counter += 1
        else:
            second_matrix_counter += 1

    return result


def csr_row_iter(csr, row_index):
    row_length = csr.shape[1]
    data_begin = csr.indptr[row_index]
    data_end = csr.indptr[row_index + 1] if row_index + 1 < csr.shape[0] else len(csr.data)

    j = 0

    for data_idx in range(data_begin, data_end):
        number = csr.indices[data_idx]
        value = csr.data[data_idx]

        while j < number:
            yield 0
            j += 1

        yield value
        j += 1

    for _ in range(j, row_length):
        yield 0


def do_lu_decomposition(A):
    shaped_A = A.shape[0]
    L = generate_identity_matrix(shaped_A, "lil")
    U = generate_empty_matrix(shaped_A, shaped_A, "lil")

    for i in range(shaped_A):
        for j, a in zip(range(shaped_A), csr_row_iter(A, i)):
            num = a - get_lil_row_product(U, L, j, i)

            if i <= j:
                U[j, i] = num
            else:
                L[i, j] = num / U[j, j]

    return L.tocsr(), U.transpose().tocsr()


def get_lower_trivial_system_solution(A, b):
    x = np.zeros(len(b))
    x[0] = b[0]

    for i in range(1, len(b)):
        x[i] = b[i] - A[i] * x

    return x


def get_upper_trivial_system_solution(A, b):
    N = len(b)
    x = np.zeros(N)
    x[-1] = b[-1] / A[-1, -1]

    for i in reversed(range(N - 1)):
        x[i] = (b[i] - A[i] * x) / A[i, i]

    return x


def get_system_solution(A, b):
    L, U = do_lu_decomposition(A)
    y = get_lower_trivial_system_solution(L, b)
    x = get_upper_trivial_system_solution(U, y)
    return x
