from unittest import TestCase

import numpy as np
from algorithms.seidel_method import process_seidel_method
from scipy.sparse import csr_matrix


class Test(TestCase):
    def test_seidel_method(self):
        # ARRANGE
        first_matrix = [[2, 1, 1], [0, 3, 2], [0, 0, 7]]
        first_vector = [9, 8, 7]
        first_expected_answer = [3, 2, 1]

        second_matrix = [[5, 1, 1], [1, 6, 2], [0, 1, 7]]
        second_vector = [7, 13, 2]
        second_expected_answer = [1, 2, 0]

        # ACT
        first_csr_matrix = csr_matrix(first_matrix)
        first_actual_answer = process_seidel_method(first_csr_matrix, first_vector, 10e-3)
        second_csr_matrix = csr_matrix(second_matrix)
        second_actual_answer = process_seidel_method(second_csr_matrix, second_vector, 10e-3)

        # ASSERT
        assert np.isclose(first_actual_answer, first_expected_answer).all()
        assert np.isclose(second_actual_answer, second_expected_answer).all()
