import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def plot_clustered_matrix(clusters, centers):
    for key, cluster, center in zip(clusters.keys(), clusters.values(), centers):
        MatrixClusterPlotter(key, cluster, center).plot()


class MatrixClusterPlotter:

    def __init__(self, key, cluster, center):
        self.fig = plt.figure()
        self.cluster = cluster
        self.key = key
        self.center = center
        self.fig.subplots_adjust(hspace=0.1, wspace=0.1)
        self.matrix_in_row = 10
        self.rows = np.ceil((len(cluster) + 2) / self.matrix_in_row)

    def plot(self):
        text = self.fig.add_subplot(self.rows, self.matrix_in_row, 1)
        text.text(0.5, 0.7, "Center: ",
                  horizontalalignment='center', verticalalignment='center')
        text.set_axis_off()
        text.set_xticks([])
        self.add_subplot_of_matrix(2, self.center)
        for i, matrix in enumerate(self.cluster):
            self.add_subplot_of_matrix(i + 3, matrix)
        plt.savefig("Cluster: " + str(self.key), bbox_inches='tight', dpi=200)

    def add_subplot_of_matrix(self, i, matrix):
        ax = self.fig.add_subplot(self.rows, self.matrix_in_row, i)
        ax.set_yticks([])
        ax.set_xticks([])
        ax.imshow(matrix, interpolation='nearest', cmap='Greys_r')
