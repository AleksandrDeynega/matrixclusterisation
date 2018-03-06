import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from kmeans import KMeans
from matrix import MatrixBuilder


def find_center(cluster):
    return np.mean(cluster, axis=0)


def distance_between(a, b):
    return abs(np.sum(a) - np.sum(b))


def init_board_gauss(N, k):
    n = float(N) / k
    X = []
    centers = []
    for i in range(k):
        c = (random.uniform(-1, 1), random.uniform(-1, 1))
        centers.append(c)
        s = random.uniform(0.05, 0.15)
        x = []
        while len(x) < n:
            a, b = np.array([np.random.normal(c[0], s), np.random.normal(c[1], s)])
            # Continue drawing points from the distribution in the range [-1,1]
            if abs(a) and abs(b) < 1:
                x.append([a, b])
        X.extend(x)
    X = np.array(X)[:N]
    return [X, centers]


def plot_board(centers, first_centers, real_centers, clusters, X):
    N = len(X)
    K = len(centers)
    fig = plt.figure(figsize=(5, 5))
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    print(type(real_centers[0]))
    if centers and clusters:
        for m, cluster in clusters.items():
            cs = cm.spectral(1. * m / K)
            plt.plot(first_centers[m][0], first_centers[m][1], '.', marker='o',
                     markersize=8, color='grey')
            plt.plot(real_centers[m][0], real_centers[m][1], '.', marker='.',
                     markersize=12, color='red')
            # plt.plot(centers[m][0], centers[m][1], 'o', marker='*',
            #          markersize=12, color=cs)
            plt.plot([point[0] for point in clusters[m]], [point[1] for point in clusters[m]], '.',
                     markersize=8, color=cs, alpha=0.5)
    else:
        plt.plot(zip(*X)[0], zip(*X)[1], '.', alpha=0.5)

    tit = 'K-means with random initialization'
    pars = 'N=%s, K=%s' % (str(N), str(K))
    plt.title('\n'.join([pars, tit]), fontsize=16)
    plt.savefig('K-means_N%s_K%s.png' % (str(N), str(K)),
                bbox_inches='tight', dpi=200)


if __name__ == "__main__":
    X = MatrixBuilder.all_binary_square_matrix_of_size_2()
    kmeans = KMeans(3, X, find_center=find_center,
                    distance_between=distance_between)
    print(kmeans.fit())
