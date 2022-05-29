from itertools import count
from timeit import timeit

from scipy.sparse import linalg

from algorithms import slau_solution, seidel_method
from algorithms.base_algorithms import generate_big_matrix, generate_random_vector

from algorithms.base_algorithms import generate_empty_matrix


def generate_nonsingular_matrix(n, p):
    matrix = generate_big_matrix(n, p, "lil")
    for i in range(n):
        matrix[i, i] += 1000
    return matrix


def generate_diagonal_domination_matrix(a, k):
    n = len(a)
    A_k = generate_empty_matrix(n, n, "lil").tolil()

    for i in range(n):
        t1 = -sum(a[i][k] for k in range(i))
        t2 = -sum(a[i][k] for k in range(i + 1, n))
        t = t1 + t2
        for j in range(n):
            if i == j:
                A_k[i, j] = t
            else:
                A_k[i, j] = t + pow(10.0, -k)

    A_k = A_k.tocsr()
    return A_k


def generate_hilbert_matrix(k):
    A_k = generate_empty_matrix(k, k, "lil").tolil()
    for i in range(k):
        for j in range(k):
            A_k[i, j] = 1.0 / (i + j + 1.0)

    return A_k.tocsr()


def test_equations(A, F):
    sum = 0.0
    left = seidel_method.process_seidel_method(A, F)
    right = slau_solution.get_system_solution(A, F)

    for i in range(left.shape[0]):
        sum += abs(right[i] - left[i])

    return sum


def generate_test_data(n, p=0.3):
    matrix = generate_nonsingular_matrix(n, p).tocsr()
    x = generate_random_vector(n)
    vector = matrix * x
    return matrix, vector


def test_exe_time(solver, matrix, vector, repeat=1):
    return timeit(lambda: solver(matrix, vector), number=repeat)


def scipy_solver(matrix, vector):
    lu = linalg.splu(matrix)
    return lu.solve(vector)


if __name__ == "__main__":
    #solver = iteration_method.seidel_method
    solver = slau_solution.get_system_solution
    # solver = seidel_method.process_seidel_method


    print("n, execution_time")
    matrix, vector = generate_test_data(100000, p=0.01)
    exe_time = test_exe_time(solver, matrix, vector)
    print(10**5, exe_time, sep=", ")
    '''
    time.sleep(5)
    for exp in count(1):
        n = 10 + exp
        matrix, vector = gen_test_data(n, p=0.01)
        exe_time = test_exe_time(solver, matrix, vector)
        print(n, exe_time, sep=", ")
    '''