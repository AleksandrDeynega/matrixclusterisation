import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


# def find_center(cluster):
#     return np.mean(cluster, axis=0)
#
#
# def distance_between(a, b):
#     return np.linalg.norm(a - b)


def init_board_gauss(N, k):
    n = float(N) / k
    X = []
    for i in range(k):
        c = (random.uniform(-1, 1), random.uniform(-1, 1))
        s = random.uniform(0.05, 0.15)
        x = []
        while len(x) < n:
            a, b = np.array([np.random.normal(c[0], s), np.random.normal(c[1], s)])
            # Continue drawing points from the distribution in the range [-1,1]
            if abs(a) and abs(b) < 1:
                x.append([a, b])
        X.extend(x)
    X = np.array(X)[:N]
    return X


def plot_board(centers, clusters, X):
    N = len(X)
    K = len(centers)
    fig = plt.figure(figsize=(5, 5))
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    if centers and clusters:
        for m, cluster in clusters.items():
            cs = cm.spectral(1. * m / K)
            plt.plot(centers[m][0], centers[m][1], 'o', marker='*',
                     markersize=12, color=cs)
            plt.plot(zip(*clusters[m])[0], zip(*clusters[m])[1], '.',
                     markersize=8, color=cs, alpha=0.5)
    else:
        plt.plot(zip(*X)[0], zip(*X)[1], '.', alpha=0.5)

    tit = 'K-means with random initialization'
    pars = 'N=%s, K=%s' % (str(N), str(K))
    plt.title('\n'.join([pars, tit]), fontsize=16)
    plt.savefig('K-means_N%s_K%s.png' % (str(N), str(K)),
                bbox_inches='tight', dpi=200)


class KMeans:
    def __init__(self, K, X=None, max_iter=100,
                 distance_between=lambda a, b: np.linalg.norm(a - b),
                 find_center=lambda cluster: np.mean(cluster, axis=0)):
        self.K = K
        if X is None:
            raise Exception("If no data is provided!")
        self.X = X
        self.distance_between = distance_between
        self.find_center = find_center
        self.max_iterations = max_iter
        self.clusters = None
        self.old_centers = None
        self.centers = None

    def _init_clusters(self):
        return {i: [] for i in range(self.K)}

    def _init_centers(self):
        # return random.sample(self.X, self.K)
        self.centers = random.sample(self.X, 1)
        while len(self.centers) < self.K:
            self.centers.append(self._find_next_center())

    def _find_next_center(self):
        D2 = self._min_squared_distances_to_centers()
        probabilities = D2 / D2.sum()
        cumulative_probabilities = probabilities.cumsum()
        r = random.random()
        next_center_index = np.where(cumulative_probabilities >= r)[0][0]
        return self.X[next_center_index]

    def _find_closest_center_key(self, x):
        return min(self._distances_to_centers(x), key=lambda t: t[1])[0]

    def _cluster_points(self):
        clusters = self._init_clusters()
        for x in self.X:
            clusters[self._find_closest_center_key(x)].append(x)
        self.clusters = clusters

    def _distances_to_centers(self, x):
        return [(i[0], self.distance_between(x, self.centers[i[0]]))
                for i in enumerate(self.centers)]

    def _min_squared_distance_to_centers(self, x):
        return min([distance[1] ** 2 for distance in self._distances_to_centers(x)])

    def _min_squared_distances_to_centers(self):
        return np.array([self._min_squared_distance_to_centers(x) for x in self.X])

    def _has_converged(self):
        return self.old_centers is not None and \
               (set([tuple(a) for a in self.centers]) ==
                set([tuple(a) for a in self.old_centers]))

    def _reevaluate_centers(self):
        self.old_centers = self.centers
        new_centers = []
        keys = sorted(self.clusters.keys())
        for k in keys:
            new_centers.append(self.find_center(self.clusters[k]))
        self.centers = new_centers

    def fit(self):
        self._init_centers()
        self.clusters = self._init_clusters()
        iterations = 0
        while not self._has_converged() and iterations < self.max_iterations:
            self._cluster_points()
            self._reevaluate_centers()
            iterations += 1
        if iterations == self.max_iterations:
            raise Exception("Max iter has been reached!")
        return self.clusters


if __name__ == "__main__":
    X = init_board_gauss(200, 5)
    kmeans = KMeans(5, X)
    plot_board(X=X, clusters=kmeans.fit(), centers=kmeans.centers)
