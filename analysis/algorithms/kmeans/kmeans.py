import pandas
import numpy as np
from sklearn.cluster import KMeans, AffinityPropagation
from sklearn.preprocessing import minmax_scale, normalize, maxabs_scale
from visualization import politic, mathematical

data = pandas.read_csv('/Users/ozzy/PycharmProjects/matrixclusterisation/data/raw/all-countries-data.csv',
                       index_col=0)


def to_clusters(labels):
    clusters = {}
    for label in set(labels):
        clusters[label] = list(data.index[np.where(labels == label)])
    return clusters


def pre_process(the_data):
    return normalize(the_data)


def split_to_matrix(the_data):
    matrix = []
    for row in the_data:
        matrix.append(np.split(row, 14))
    return matrix


preproc_data = pre_process(data)

list_of_matrix = split_to_matrix(preproc_data)


def main():
    alg = KMeans(n_clusters=3, n_init=40)
    # alg = AffinityPropagation(affinity='precomputed')
    alg.fit(preproc_data)
    mathematical.plot_clusters(data, alg.labels_)
    politic.plot_clusters(alg.labels_)
    # for c in to_clusters(alg.labels_).values():
    #     print(', '.join(c))


if __name__ == '__main__':
    main()
