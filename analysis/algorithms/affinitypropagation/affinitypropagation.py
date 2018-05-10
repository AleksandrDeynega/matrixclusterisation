from sklearn.cluster import AffinityPropagation
import distances
import utils
import visualization.mathematical
from analysis.constants import list_of_matrix

if __name__ == '__main__':
    X = list_of_matrix
    af = AffinityPropagation(affinity='precomputed')
    af.fit(utils.build_affinity_matrix(X, distances.form_difference))
    print(af.labels_)
    centers = utils.build_centers(af.cluster_centers_indices_, X)
    clusters = utils.build_clusters(af.labels_, X)
    visualization.mathematical.plot_clustered_matrix(clusters, centers)
