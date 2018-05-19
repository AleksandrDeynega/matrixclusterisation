import numpy as np


def distance_matrix(X, norm=np.linalg.norm):
    X = np.array(X)
    return np.array([[norm(a - b) for b in X] for a in X])


def similarity_matrix(X, similarity=lambda a, b: 1 / np.linalg.norm(a - b),
                      norm=None):
    X = np.array(X)
    # if norm:
    #     similarity = lambda a, b: 1.0 / norm(a - b) ^ 2
    return np.array([[similarity(a, b) for b in X] for a in X])
