from unittest import TestCase

import numpy as np
from algorithms.base_algorithms import generate_empty_matrix, generate_identity_matrix, generate_hilbert_matrix


class Test(TestCase):
    def test_empty_matrix(self):
        # ARRANGE
        expected_array = np.array([[0, 0, 0], [0, 0, 0]])

        # ACT
        result = generate_empty_matrix(2, 3, "csr")

        # ASSERT
        assert (result == expected_array).all()
        assert result.getformat() == "csr"

    def test_identity_matrix(self):
        # ARRANGE
        expected_array = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

        # ACT
        result = generate_identity_matrix(3, "csr")

        # ASSERT
        assert (result == expected_array).all()
        assert result.getformat() == "csr"

    def test_generate_hilbert_matrix(self):
        # ARRANGE
        expected_array = np.array(
            [
                [1, 1 / 2, 1 / 3, 1 / 4, 1 / 5],
                [1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6],
                [1 / 3, 1 / 4, 1 / 5, 1 / 6, 1 / 7],
                [1 / 4, 1 / 5, 1 / 6, 1 / 7, 1 / 8],
                [1 / 5, 1 / 6, 1 / 7, 1 / 8, 1 / 9],
            ]
        )

        # ACT
        result = generate_hilbert_matrix(5).toarray()

        # ASSERT
        assert np.allclose(expected_array, result)
