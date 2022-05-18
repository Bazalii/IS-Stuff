from unittest import TestCase

import numpy as np
from algorithms.slau_solution import (
    csr_row_iter,
    get_lower_trivial_system_solution,
    do_lu_decomposition,
    get_system_solution,
    get_upper_trivial_system_solution,
)
from scipy.sparse import csr_matrix


class Test(TestCase):
    def test_lu_decomposition(self):
        # ARRANGE
        matrix = csr_matrix(
            np.array(
                [
                    [3, 4, -9, 5],
                    [-15, -12, 50, -16],
                    [-27, -36, 73, 8],
                    [9, 12, -10, -16],
                ]
            )
        )

        expected_lower_matrix = np.array(
            [
                [1, 0, 0, 0],
                [-5, 1, 0, 0],
                [-9, 0, 1, 0],
                [3, 0, -17 / 8, 1],
            ]
        )

        expected_upper_matrix = np.array(
            [
                [3, 4, -9, 5],
                [0, 8, 5, 9],
                [0, 0, -8, 53],
                [0, 0, 0, 653 / 8],
            ]
        )

        # ACT
        result_lower_matrix, result_upper_matrix = do_lu_decomposition(matrix)
        result_lower_matrix = result_lower_matrix.toarray()
        result_upper_matrix = result_upper_matrix.toarray()

        # ASSERT
        assert np.isclose(result_lower_matrix, expected_lower_matrix).all()
        assert np.isclose(result_upper_matrix, expected_upper_matrix).all()

    def test_csr_row_iter(self):
        # ARRANGE
        expected_values = [0, 0, 1, 2, 0, 3, 0, 0]

        # ACT
        result_matrix = csr_matrix([expected_values])
        generated_rows = csr_row_iter(result_matrix, 0)
        result_values = list(generated_rows)

        # ASSERT
        assert result_values == expected_values

    def test_upper_trivial_system_solution(self):
        # ARRANGE
        input_matrix = csr_matrix(np.array([[2, 1, 1], [0, 3, 2], [0, 0, 7]]))
        input_vector = np.array([9, 8, 7])
        expected_solution = np.array([3, 2, 1])

        # ACT
        result = get_upper_trivial_system_solution(input_matrix, input_vector)

        # ASSERT
        assert np.isclose(result, expected_solution).all()

    def test_lower_trivial_system_solution(self):
        # ARRANGE
        input_matrix = csr_matrix(np.array([[1, 0, 0], [2, 1, 0], [3, 2, 1]]))
        input_vector = np.array([1, 3, 9])
        expected_solution = np.array([1, 1, 4])

        # ACT
        actual = get_lower_trivial_system_solution(input_matrix, input_vector)

        # ASSERT
        assert np.isclose(actual, expected_solution).all()

    def test_system_solution(self):
        # ARRANGE
        first_matrix = [[5, 7, 4], [9, 5, 7], [1, 2, 7]]
        first_vector = [4, 5, 2]
        first_answer = [63.0 / 235, 67.0 / 235, 39.0 / 235]

        second_matrix = [[7, 7, 30], [4, 7, 9], [7, 1, 30]]
        second_vector = [-6, 6, 3]
        second_answer = [303.0 / 38, -3.0 / 2, -65.0 / 38]

        # ACT
        first_csr_matrix = csr_matrix(first_matrix)
        first_result = get_system_solution(first_csr_matrix, first_vector)
        second_csr_matrix = csr_matrix(second_matrix)
        second_result = get_system_solution(second_csr_matrix, second_vector)

        # ASSERT
        assert np.isclose(first_result, first_answer).all()
        assert np.isclose(second_result, second_answer).all()
