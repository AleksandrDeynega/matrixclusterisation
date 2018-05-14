import pandas

indicators = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6',
              'P2', 'P4a', 'P5a',
              'C1a', 'C1b', 'C1c', 'C1d']

sectors = ['%.2d' % i for i in range(1, 15)]

headers = ['N', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'P1', 'P2', 'P3', 'P4a', 'P4b',
           'P5a', 'P5b', 'C1', 'C1a', 'C1b', 'C1c', 'C1d', 'C2', 'A', 'P', 'C']


def get_list_of_countries():
    with open('/Users/ozzy/PycharmProjects/matrixclusterisation/scrapping/constants/sub-saharan africa.csv',
              'r') as file:
        return [line.strip() for line in file]


list_of_countries = get_list_of_countries()

path_to_countries = '/Users/ozzy/PycharmProjects/matrixclusterisation/data/normalized/countries/{}.csv'

list_of_matrix = [pandas.read_csv(path_to_countries.format(country), index_col=0).values
                  for country in list_of_countries]

if __name__ == '__main__':
    print(pandas.read_csv(path_to_countries.format('Angola'), index_col=0).index)
    print(sectors)