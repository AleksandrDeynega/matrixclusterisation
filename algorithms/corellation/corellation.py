import pandas
from scrapping.constants import list_of_countries, sectors, headers
import matplotlib.pyplot as plt
import seaborn as sns

needed_headers = headers[1:11] + headers[12:13] + headers[14:-4]


def main():
    frames = []
    for country in list_of_countries:
        frames.append(pandas.read_csv(
            '/Users/ozzy/PycharmProjects/matrixclusterisation/data/countries/{}.csv'.format(country),
            index_col=0
        ).loc[sectors, needed_headers])
    result = pandas.concat(frames)
    corr = result.corr()
    sns.heatmap(corr,
                xticklabels=needed_headers,
                yticklabels=needed_headers)
    plt.show()


if __name__ == '__main__':
    main()
