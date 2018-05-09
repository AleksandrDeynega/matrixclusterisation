import csv


def get_country_number_map_from_file():
    return {row[0]: row[1] for row in csv.reader(open('/Users/ozzy/PycharmProjects/matrixclusterisation/scrapping/constants/country-number.csv'))}


def get_list_of_countries():
    with open('/Users/ozzy/PycharmProjects/matrixclusterisation/scrapping/constants/sub-saharan africa.csv', 'r') as file:
        return [line.strip() for line in file]


url = "https://tradecompetitivenessmap.intracen.org/TPIC.aspx"

sectors = ["%.2d" % i for i in range(1, 15)]

headers = ['N', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'P1', 'P2', 'P3', 'P4a', 'P4b',
           'P5a', 'P5b', 'C1', 'C1a', 'C1b', 'C1c', 'C1d', 'C2', 'A', 'P', 'C']

index = [f(sector) for sector in sectors for f in [lambda x: x, lambda x: x + '_rank']]

country_number_map = get_country_number_map_from_file()

list_of_countries = get_list_of_countries()
