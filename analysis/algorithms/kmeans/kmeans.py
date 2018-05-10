import pandas
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import Normalizer
from visualization.politic.politic import plot_clusters
from analysis.constants import indicators
from scrapping.constants import sectors

data = pandas.read_csv('/Users/ozzy/PycharmProjects/matrixclusterisation/data/all-countries-data.csv', index_col=0)
data = data.loc[:, [sector + indicator for sector in sectors for indicator in indicators]]


def to_clusters(labels):
    clusters = {}

    for label in set(labels):
        clusters[label] = list(data.index[np.where(labels == label)])
    return clusters


def main():
    kmeans = KMeans(n_clusters=3, n_init=40)
    kmeans.fit(Normalizer().fit_transform(data))
    # kmeans.fit(data)
    plot_clusters(to_clusters(kmeans.labels_))


if __name__ == '__main__':
    main()
