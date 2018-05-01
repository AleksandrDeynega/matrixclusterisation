import pandas
from scrapping.constants import index, headers, sectors, url, country_number_map, list_of_countries


def main():
    for country in list_of_countries:
        df = pandas.read_csv("countries/{}.csv".format(country), index_col=0).transpose()
        print(df.loc[['G1'], sectors])


if __name__ == '__main__':
    main()
