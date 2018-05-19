import pandas
import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import minmax_scale, normalize, maxabs_scale
from visualization import politic, mathematical

data = pandas.read_csv('/Users/ozzy/PycharmProjects/matrixclusterisation/data/raw/all-countries-data.csv',
                       index_col=0)

def split_to_matrix(the_data):
    matrix = []
    for row in the_data:
        matrix.append(np.split(row, 14))
    return np.array(matrix)


data = normalize(data)
matrices = split_to_matrix(data)

kmeans = KMeans(n_clusters=3, n_init=40)
kmeans.fit(data)
mathematical.plot_clusters(matrices, kmeans.labels_)
politic.plot_clusters(kmeans.labels_)

kmeans.