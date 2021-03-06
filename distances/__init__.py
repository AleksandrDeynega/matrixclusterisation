import numpy as np


def find_center(cluster):
    return np.mean(cluster, axis=0)


def form_difference(a, b):
    return np.mean(abs(np.matrix(b) - np.matrix(a)))


def sums_difference(a, b):
    return abs(np.sum(b) - np.sum(a))


def max_col_sum(a, b):
    return np.sum(b, axis=1).max() - np.sum(a, axis=1).max()
