import pandas
import numpy as np
from analysis.constants import sectors, indicators
from sklearn.preprocessing import normalize, minmax_scale

if __name__ == '__main__':
    data = pandas.read_csv('raw/all-countries-data.csv',
                           index_col=0)
    # data = minmax_scale()

    # for country in data.index:
    #     values = np.split(data.loc[country].values, 14)
    #     pandas.DataFrame(values, columns=indicators, index=sectors) \
    #         .to_csv('normalized/countries/{}.csv'.format(country))
