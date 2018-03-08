import numpy as np
import matplotlib.pyplot as plt
import visualization
import utils

from kmeans import KMeans
from matrix import MatrixBuilder


def find_center(cluster):
    return np.mean(cluster, axis=0)


def form_difference(a, b):
    return np.mean(abs(np.matrix(b) - np.matrix(a)))


def sums_difference(a, b):
    return abs(np.sum(b) - np.sum(a))


if __name__ == "__main__":
    X = MatrixBuilder.all_binary_square_matrix_of_size(3)
    kmeans = KMeans(8, X, find_center=find_center,
                    distance_between=form_difference)
    clusters = kmeans.fit()
    utils.print_clustered_matrix_by_rows(10, clusters, kmeans.centers)
    visualization.plot_clustered_matrix(clusters, kmeans.centers)
