import pandas
from scrapping.constants import list_of_countries, sectors, headers
import matplotlib.pyplot as plt
import seaborn as sns
from analysis.constants import indicators

# needed_headers = headers[1:11] + headers[12:13] + headers[14:-4]


needed_headers = indicators

def main():
    frames = []
    for country in list_of_countries:
        frames.append(pandas.read_csv(
            '/Users/ozzy/PycharmProjects/matrixclusterisation/data/bad/countries/{}.csv'.format(country),
            index_col=0
        ).loc[sectors, needed_headers])
    result = pandas.concat(frames)
    corr = result.corr()
    print(corr)
    sns.heatmap(corr,
                xticklabels=needed_headers,
                yticklabels=needed_headers)
    plt.show()


if __name__ == '__main__':
    main()
