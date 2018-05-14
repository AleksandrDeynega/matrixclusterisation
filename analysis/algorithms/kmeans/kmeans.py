import pandas
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import minmax_scale, normalize, maxabs_scale
from analysis.constants import list_of_countries, sectors, indicators
from visualization import politic, mathematical
from utils import build_centers, build_clusters
from analysis.constants import list_of_matrix

data = pandas.read_csv('/Users/ozzy/PycharmProjects/matrixclusterisation/data/normalized/all-countries-data.csv',
                       index_col=0)


def to_clusters(labels):
    clusters = {}
    for label in set(labels):
        clusters[label] = list(data.index[np.where(labels == label)])
    return clusters


def main():
    kmeans = KMeans(n_clusters=4, n_init=40)
    kmeans.fit(min_max_scaled_data())
    mathematical.plot_clusters(build_clusters(kmeans.labels_, list_of_matrix))
    politic.plot_clusters(to_clusters(kmeans.labels_))


def min_max_scaled_data():
    df = pandas.read_csv('/Users/ozzy/PycharmProjects/matrixclusterisation/data/raw/all-countries-data.csv',
                         index_col=0) \
        .loc[list_of_countries,
             [sector + indicator for indicator in indicators for sector in sectors]]
    return minmax_scale(df)


if __name__ == '__main__':
    main()
