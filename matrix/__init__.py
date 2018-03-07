import numpy as np


class MatrixBuilder:

    @staticmethod
    def all_binary_square_matrix_of_size(n):
        X = []
        shift = np.arange(n * n).reshape(n, n)
        for j in range(2 ** (n * n)):
            X.append(j >> shift & 1)
        return X
