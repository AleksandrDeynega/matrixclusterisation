import matplotlib.pyplot as plt
import numpy as np
import csv
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from scrapping.constants import list_of_countries

map = Basemap(width=12000000, height=9000000, projection='lcc',
              resolution='c', lat_1=30., lat_2=30., lat_0=-10., lon_0=20.)

# map.bluemarble()
map.shadedrelief()

ax = plt.gca()
map.readshapefile('/Users/ozzy/PycharmProjects/matrixclusterisation/visualization/politic/Africa_SHP/Africa',
                  name='Africa', drawbounds=False)
country_codes = []
for shape_dict in map.Africa_info:
    country_codes.append(shape_dict['CODE'])


def get_country_code_dict():
    return {row[0]: row[1] for row in
            csv.reader(open('/Users/ozzy/PycharmProjects/matrixclusterisation/visualization/politic/counrty-code.csv'))}


country_code_dict = get_country_code_dict()


def add_countries(countries, color):
    for country in countries:
        add_country(country, color)


def plot_clusters(clusters):
    # colors = ['aqua', 'orangered', 'lime', 'chartreuse', 'lavender']
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    for label, countries in zip(clusters.keys(), clusters.values()):
        add_countries(countries, colors[label])
        # add_countries(countries, np.random.rand(3))
    plt.show()


def add_country(country, color):
    if country == "Seychelles" or country == "Mauritius":
        return
    seg = map.Africa[country_codes.index(country_code_dict[country])]
    poly = Polygon(seg, facecolor=color, edgecolor=color)
    poly.set_alpha(0.4)
    ax.add_patch(poly)


if __name__ == '__main__':
    print(map.Africa_info)
    # add_country('Niger', np.random.rand(1, 3))

    # map.shadedrelief()
    # map.drawrivers()

    # plt.show()
    # country_codes = []
    # for shape_dict in map.Africa_info:
    #     country_codes.append(shape_dict['CODE'])
    # print(len(set(country_names)))
    # print(len(set(country_codes)))
    # print(set(list_of_countries).difference(set(country_names)))
    # country_name_code_dict = {}
    # for shape_dict in map.Africa_info:
    #     country_name_code_dict[shape_dict['COUNTRY']] = shape_dict['CODE']

    # with open('counrty-code.csv', 'w') as file:
    #     for country, code in zip(country_name_code_dict.keys(), country_name_code_dict.values()):
    #         file.write((",".join([country, code]) + "\n"))
