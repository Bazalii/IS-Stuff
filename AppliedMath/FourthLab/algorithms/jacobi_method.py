import numpy as np

import matplotlib.pyplot as plt

import math

from algorithms.base_algorithms import *


def find_max_element(a):  # Find largest off-diag. element a[k,l]
    n = a.shape[0]
    a_max = 0.0
    k = 0
    l = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(a[i, j]) >= a_max:
                a_max = abs(a[i, j])
                k = i
                l = j
    return a_max, k, l


def check_end(matrix, p):
    tmp = 0
    n = matrix.shape[0]

    for i in range(n - 1):
        for j in range(i + 1, n):
            tmp += matrix[i, j] ** 2

    return round(tmp ** 0.5, p + 1) <= 10 ** (-p)


def process_jacobi_method(matrix, p=3):
    n = matrix.shape[0]
    maximum = 10 ** 7

    for i in range(maximum):
        lil_matrix_k = generate_identity_matrix(n, "lil")
        aMax, k, l = find_max_element(matrix)

        if matrix[k, k] == matrix[l, l]:
            phi_k = math.pi / 4
        else:
            phi_k = 0.5 * math.atan(2 * matrix[k, l] / (matrix[k, k] - matrix[l, l]))

        lil_matrix_k[k, k] = math.cos(phi_k)
        lil_matrix_k[k, l] = -1. * math.sin(phi_k)
        lil_matrix_k[l, k] = math.sin(phi_k)
        lil_matrix_k[l, l] = math.cos(phi_k)

        lil_matrix_k_transposed = lil_matrix_k.transpose()

        matrix = lil_matrix_k_transposed * matrix * lil_matrix_k
        # counter += 1

        if check_end(matrix, p):
            print(f"Jacobi method converges with {i} iterations")
            return matrix, i
    print(f"Jacobi method diverges. Iterations: {maximum}.")
    return None, maximum


if __name__ == "__main__":
    N = 10
    diap = range(3, N, 3)
    data = []
    tolerances = [3, 6, 9]
    total_iterations = []

    for tolerance in tolerances:
        for n in diap:
            matrix, iterations = process_jacobi_method(generate_hilbert_matrix(n), tolerance)
            data.append(iterations)
    plt.figure(figsize=(12, 7))

    y_label = "Вращения"
    flag = y_label != "Вращения"

    graph_data = []
    print(total_iterations)
    iterator = 0
    for i in range(len(tolerances)):
        graph_data = []
        for n in diap:
            graph_data.append(data[iterator])
            iterator += 1
        plt.plot(list(diap), graph_data, label="tol=" + str(10 ** (-tolerances[i])))

    plt.xlabel("Размер матрицы", fontsize=18)
    plt.ylabel(y_label, fontsize=18)
    plt.legend()
    plt.show()
