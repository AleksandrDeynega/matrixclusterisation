import pandas
from scrapping.constants import headers, sectors, list_of_countries

needed_headers = headers[1:11] + headers[12:13] + headers[14:-4]

needed_columns = [sector + header for sector in sectors for header in needed_headers]

columns = [sector + header for sector in sectors for header in needed_headers]


def clean(df):
    df = df.applymap(lambda x: str(x).replace(' ', '0'))
    df = df.applymap(lambda x: str(x).replace('\xa0', '0'))
    df = df.applymap(lambda x: str(x).replace(',', '').replace('%', ''))
    df = df.applymap(pandas.to_numeric)
    return df


def main():
    pass
    # print(pandas.read_csv('data/all-countries-data.csv', index_col=0).head())
    # transform_all_countries_to_one_df().to_csv("all-countries-data.csv")


def transform_all_countries_to_one_df():
    data_array = []
    for country in list_of_countries:
        df = pandas.read_csv("data/countries/{}.csv".format(country), index_col=0)
        data_array.append(df.loc[sectors, needed_headers].values.ravel())
    return pandas.DataFrame(data=data_array, columns=needed_columns, index=list_of_countries)


def clean__and_save_all_countries():
    for country in list_of_countries:
        df = pandas.read_csv("countries/{}.csv".format(country), index_col=0)
        pandas.DataFrame(clean(df)).to_csv("data/countries/{}.csv".format(country))


if __name__ == '__main__':
    main()
