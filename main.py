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
    return np.mean(abs(np.matrix(b) - np.matrix(a)))


if __name__ == "__main__":
    X = MatrixBuilder.all_binary_square_matrix_of_size_2()
    kmeans = KMeans(4, X, find_center=find_center,
                    distance_between=distance_between)
    # utils.print_matrix(X[0])
    # utils.print_matrix(X[15])
    # print (distance_between(X[0], X[15]))
    # print (abs(np.matrix(X[0]) - np.matrix(X[15])))
    utils.print_full_info_clustered_matrix(kmeans.fit())
