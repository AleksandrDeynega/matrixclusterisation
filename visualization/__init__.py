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
        self.rows = 1 + (np.ceil((len(cluster)) / self.matrix_in_row))

    def plot(self):
        text = self.fig.add_subplot(self.rows, self.matrix_in_row, 1)
        text.text(0.5, 0.7, self.title(),
                  horizontalalignment='center', verticalalignment='center')
        text.set_axis_off()
        self.add_subplot_of_matrix(3, self.center)
        for i, matrix in enumerate(self.cluster):
            self.add_subplot_of_matrix(i + 11, matrix)
        plt.savefig("Cluster: " + str(self.key), bbox_inches='tight', dpi=200)

    def title(self):
        return "\n".join(["Center " + str(self.key) + " : ",
                          "Lenght :" + str(len(self.cluster))])

    def add_subplot_of_matrix(self, i, matrix):
        ax = self.fig.add_subplot(self.rows, self.matrix_in_row, i)
        ax.set_yticks([])
        ax.set_xticks([])
        ax.imshow(matrix, interpolation='nearest', cmap='Greys_r')
