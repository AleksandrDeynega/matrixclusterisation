import pandas
import numpy as np
from analysis.constants import sectors, indicators, list_of_countries
from sklearn.preprocessing import normalize, minmax_scale

if __name__ == '__main__':
    df = pandas.read_csv('/Users/ozzy/PycharmProjects/matrixclusterisation/data/bad/countries/Botswana.csv',
                         index_col=0) \
        .loc[sectors, indicators]
    print(df)
    # df.to_csv('raw/all-countries-data.csv')

    # df = pandas.read_csv('/Users/ozzy/PycharmProjects/matrixclusterisation/data/bad/all-countries-data.csv',
    #                      index_col=0) \
    #     .loc[list_of_countries,
    #          [sector + indicator for sector in sectors for indicator in indicators]]
    # df.to_csv('raw/all-countries-data.csv')

    # for country in data.index:
    #     values = np.split(data.loc[country].values, 14)
    #     pandas.DataFrame(values, columns=indicators, index=sectors) \
    #         .to_csv('normalized/countries/{}.csv'.format(country))
