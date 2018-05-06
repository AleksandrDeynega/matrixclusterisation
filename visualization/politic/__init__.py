import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


def main():
    print(np.array([]))
    map = Basemap()
    map.drawcoastlines()

    plt.show()
    # plt.savefig('test.png')


if __name__ == '__main__':
    main()
