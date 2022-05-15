import numpy as np
from unittest import TestCase
from algorithms.inverse_matrix_algorithm import get_inverse_matrix
from scipy.sparse import csr_matrix


class Test(TestCase):
    def test_inverse_matrix(self):
        # ARRANGE
        first_matrix = [[2, 5, 7], [6, 3, 4], [5, -2, -3]]
        first_expected_inverse = [[1, -1, 1], [-38, 41, -34], [27, -29, 24]]

        second_matrix = [[1.0, 2.0, 3.0], [3.0, 2.0, 1.0], [0.0, 1.0, 0.0]]
        second_expected_inverse = [
            [-1.0 / 8, 3.0 / 8, -1.0 / 2],
            [0.0, 0.0, 1.0],
            [3.0 / 8, -1.0 / 8, -1.0 / 2],
        ]

        third_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        third_expected_inverse = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

        # ACT
        first_csr_matrix = csr_matrix(first_matrix)
        first_actual_inverse = get_inverse_matrix(first_csr_matrix).toarray()
        second_csr_matrix = csr_matrix(second_matrix)
        second_actual_inverse = get_inverse_matrix(second_csr_matrix).toarray()
        third_csr_matrix = csr_matrix(third_matrix)
        third_actual_inverse = get_inverse_matrix(third_csr_matrix).toarray()

        # ASSERT
        assert np.isclose(first_actual_inverse, first_expected_inverse).all()
        assert np.isclose(second_actual_inverse, second_expected_inverse).all()
        assert np.isclose(third_actual_inverse, third_expected_inverse).all()
