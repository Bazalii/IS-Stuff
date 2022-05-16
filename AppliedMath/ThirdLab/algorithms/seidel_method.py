import numpy as np


def process_seidel_row_vec_product(csr, first_vector, second_vector, row_index):
    begin_index = csr.indptr[row_index]
    end_index = csr.indptr[row_index + 1] if row_index + 1 < csr.shape[0] else len(csr.data)

    curr_vector = first_vector
    product = 0
    diagonal_value = 0
    counter = 0

    for i in range(begin_index, end_index):
        column_index = csr.indices[i]
        value = csr.data[i]

        if column_index >= row_index:
            curr_vector = second_vector

        if column_index == row_index:
            diagonal_value = value
            continue

        product += value * curr_vector[column_index]

    return product, diagonal_value


def process_seidel_method(A, b, eps=1e-6, maximum_iterations_number=250):
    n = A.shape[0]
    x = np.array(b)

    for _ in range(maximum_iterations_number):
        x_new = np.zeros(n)
        for i in range(n):
            product, diagonal_value = process_seidel_row_vec_product(A, x_new, x, i)
            x_new[i] = (b[i] - product) / diagonal_value

        if np.allclose(x, x_new, rtol=eps):
            break

        x = x_new
    else:
        raise RuntimeError("Seidel method diverges!")

    return x
