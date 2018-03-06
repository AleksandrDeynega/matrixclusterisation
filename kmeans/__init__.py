import random
import numpy as np


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
        self.centers = random.sample(list(self.X), 1)
        while len(self.centers) < self.K:
            self.centers.append(self._find_next_center())
        self.first_centers = self.centers

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
               (set([tuple([tuple(a[0]), tuple(a[1])]) for a in self.centers]) ==
                set([tuple([tuple(a[0]), tuple(a[1])]) for a in self.old_centers]))

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
