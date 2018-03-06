import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from kmeans import KMeans
from matrix import MatrixBuilder
import utils


def find_center(cluster):
    return np.mean(cluster, axis=0)


def distance_between(a, b):
    return abs(np.mean(np.matrix(a) - np.matrix(b)))


if __name__ == "__main__":
    X = MatrixBuilder.all_binary_square_matrix_of_size_2()
    kmeans = KMeans(3, X, find_center=find_center,
                    distance_between=distance_between)
    utils.print_clustered_matrix(kmeans.fit())
