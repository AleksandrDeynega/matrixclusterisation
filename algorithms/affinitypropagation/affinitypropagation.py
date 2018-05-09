import random
import pandas

from sklearn.cluster import AffinityPropagation

import distances
import utils
import visualization.mathematical
from matrix import MatrixBuilder

if __name__ == '__main__':
    af = AffinityPropagation(affinity='')



    # X =
    # af = AffinityPropagation(affinity='precomputed')
    # af.fit(utils.build_affinity_matrix(X, distances.form_difference))
    # print(af.labels_)
    # centers = utils.build_centers(af.cluster_centers_indices_, X)
    # clusters = utils.build_clusters(af.labels_, X)
    # visualization.mathematical.plot_clustered_matrix(clusters, centers)
