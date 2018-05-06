import pandas
from sklearn.cluster import KMeans
from sklearn.preprocessing import Normalizer


def main():
    data = Normalizer().fit_transform(
        X=pandas.read_csv('/Users/ozzy/PycharmProjects/matrixclusterisation/data/all-countries-data.csv', index_col=0))

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data)
    print(kmeans.labels_)


if __name__ == '__main__':
    main()
