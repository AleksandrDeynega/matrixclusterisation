import random
import visualization
import utils
import distances

from sklearn.cluster import AffinityPropagation

from matrix import MatrixBuilder

if __name__ == "__main__":
    X = random.sample(MatrixBuilder.all_binary_square_matrix_of_size(3), 40)

    af = AffinityPropagation(affinity='precomputed')
    af.fit(utils.build_affinity_matrix(X, distances.form_difference))

    print(af.cluster_centers_indices_)
    print(af.labels_)

    clusters = utils.build_clusters(af.labels_, X)
    centers = utils.build_centers(af.cluster_centers_indices_, X)

    visualization.plot_clustered_matrix(clusters, centers)


    # utils.print_clustered_matrix_by_rows(clusters, kmeans.best_centers)
    # X = MatrixBuilder.all_binary_square_matrix_of_size(3)
    # kmeans = KMeans(4, X, find_center=find_center,
    #                 distance_between=form_difference)
    # clusters = kmeans.fit()
