import pandas
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import Normalizer
from visualization.politic.politic import plot_clusters

data = pandas.read_csv('/Users/ozzy/PycharmProjects/matrixclusterisation/data/all-countries-data.csv', index_col=0)


def to_clusters(labels):
    clusters = {}

    for label in set(labels):
        clusters[label] = list(data.index[np.where(labels == label)])
    return clusters


def main():
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(Normalizer().fit_transform(data))
    # kmeans.fit(data)
    plot_clusters(to_clusters(kmeans.labels_))


if __name__ == '__main__':
    main()
