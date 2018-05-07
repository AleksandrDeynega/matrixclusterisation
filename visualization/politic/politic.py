import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

ax = plt.gca()


def add_country(segment, facecolor):
    ax.add_patch(segment, facecolor=facecolor)


def main():
    # create the map
    map = Basemap(width=12000000, height=9000000, projection='lcc',
                  resolution='c', lat_1=30., lat_2=30., lat_0=-10., lon_0=20.)
    # map.drawcoastlines()
    map.readshapefile('Africa_SHP/Africa', name='Africa', drawbounds=True)

    country_names = []
    for shape_dict in map.Africa_info:
        country_names.append(shape_dict['COUNTRY'])

    ax = plt.gca()  # get current axes instance

    # get Angola and draw the filled polygon
    seg = map.Africa[country_names.index('Angola')]
    poly = Polygon(seg, facecolor='red', edgecolor='red')
    ax.add_patch(poly)

    plt.show()

if __name__ == '__main__':
    main()
