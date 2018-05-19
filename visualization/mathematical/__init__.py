import numpy as np
import matplotlib.pyplot as plt
from utils import build_clusters


def _plot_clusters(clusters):
    for key, cluster in zip(clusters.keys(), clusters.values()):
        MatrixClusterPlotter(key, cluster).plot()


def plot_clusters(data, labels):
    _plot_clusters(build_clusters(labels, data))


class MatrixClusterPlotter:
    def __init__(self, key, cluster):
        self.fig = plt.figure()
        self.cluster = cluster
        self.key = key
        self.fig.subplots_adjust(hspace=0.1, wspace=0.1)
        self.matrix_in_row = 4
        self.rows = 1 + (np.ceil((len(cluster)) / self.matrix_in_row))

    def plot(self):
        text = self.fig.add_subplot(self.rows, self.matrix_in_row, 1)
        text.text(0.5, 0.7, self.title(),
                  horizontalalignment='center', verticalalignment='center')
        text.set_axis_off()

        print("length: {}".format(len(self.cluster)))
        for i, matrix in enumerate(self.cluster):
            self.add_subplot_of_matrix(i + self.matrix_in_row + 1, matrix)
        plt.savefig(
            "/Users/ozzy/PycharmProjects/matrixclusterisation/visualization/mathematical/output/Cluster: " + str(
                self.key), bbox_inches='tight', dpi=200)

    def title(self):
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        return "\n".join(["Cluster " + colors[self.key] + " : ",
                          "Length :" + str(len(self.cluster))])

    def add_subplot_of_matrix(self, i, matrix):
        ax = self.fig.add_subplot(self.rows, self.matrix_in_row, i)
        ax.set_yticks([])
        ax.set_xticks([])
        # print("Matrix :")
        # print(matrix)
        ax.imshow(matrix, interpolation='nearest', cmap='Greys')
