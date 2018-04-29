from bs4 import BeautifulSoup
import requests
import pandas
import logging as log

url = "https://tradecompetitivenessmap.intracen.org/TPIC.aspx"
sectors = ["%.2d" % i for i in range(1, 2)]
headers = ['N', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'P1', 'P2', 'P3', 'P4a', 'P4b',
           'P5a', 'P5b', 'C1', 'C1a', 'C1b', 'C1c', 'C1d', 'C2', 'A', 'P', 'C']


# def url(country):
#     return base_url + "?RP=00{}".format(country)


def print_values(soup):
    rows = soup.find("table", {"id": "RadGrid1_ctl01"}).tbody.findAll("tr")
    for row in rows:
        print("{}       {}".format(row.findAll("td")[3].text, row.findAll("td")[4].text))


def to_array(soup):
    rows = soup.find("table", {"id": "RadGrid1_ctl01"}).tbody.findAll("tr")
    return [[row.findAll("td")[3].text for row in rows],
            [row.findAll("td")[4].text for row in rows]]


def main():
    with requests.Session() as session:
        response = session.get(url)
        data = basic_data(BeautifulSoup(response.content, "lxml"))
        values_of_country = []
        country = '076'
        for sector in sectors:
            log.info("Parsing sector: %s", sector)
            response = session.post(url, data=build_data(data, sector, country))
            soup = BeautifulSoup(response.content, "lxml")
            values_of_country += to_array(soup)
        pandas.DataFrame(values_of_country, columns=headers).to_csv("countries/{}".format(country), index=False)
        print(pandas.read_csv("countries/{}".format(country)))


def build_data(data, sector, country, year=2016):
    data['dropReporter'] = country
    data['dropYear'] = year
    data['lbxSector'] = sector
    return data


def basic_data(soup):
    return {'__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': soup.find('input', {'name': '__VIEWSTATE'}).get('value', ''),
            '__VIEWSTATEGENERATOR': soup.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value', ''),
            '__EVENTVALIDATION': soup.find('input', {'name': '__EVENTVALIDATION'}).get('value', ''),
            'TradeComTabs1$RadTabStrip1:': '{"State":{},"TabState":{"TradeComTabs1_RadTabStrip1_tabTPI":{"Selected":true},"TradeComTabs1_RadTabStrip1_tabTPI_tabTPIC":{"Selected":true}}}',
            'btnRedo': 'Redo'}


def get_country_number_map():
    with requests.Session() as session:
        response = session.get(url)
        soup = BeautifulSoup(response.content, "lxml")
        country_number = {tag.text: tag['value'] for tag in
                          soup.find("select", {"id": "dropReporter"}).findAll("option")}
    return country_number


if __name__ == '__main__':
    log.basicConfig(level=log.INFO)
    # get_country_number_map()
    # main()
