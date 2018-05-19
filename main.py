import random

from sklearn.cluster import AffinityPropagation

import distances
import utils
import visualization.mathematical
from matrix import MatrixBuilder

if __name__ == "__main__":
    X = random.sample(MatrixBuilder.all_binary_square_matrix_of_size(3), 40)

    # db = DBSCAN(eps=0.4, min_samples=3, metric='precomputed')
    # db.fit(utils.build_distance_matrix(X, distances.form_difference))
    # print(db.labels_)
    # clusters = utils.build_clusters(db.labels_, X)
    # centers = [distances.find_center(cluster) for cluster in clusters.values()]
    # visualization.plot_clustered_matrix(clusters, centers)

    af = AffinityPropagation(affinity='precomputed')
    af.fit(utils.build_affinity_matrix(X, distances.form_difference))
    print(af.labels_)
    centers = utils.build_centers(af.cluster_centers_indices_, X)
    clusters = utils.build_clusters(af.labels_, X)
    visualization.mathematical.plot_clusters(clusters)


    # kmeans = KMeans(4, X, find_center=find_center,
    #                 distance_between=form_difference)
    # clusters = kmeans.fit()
    # utils.print_clustered_matrix_by_rows(clusters, kmeans.best_centers)
    # visualization.plot_clustered_matrix(clusters, kmeans.best_centers)
