from bs4 import BeautifulSoup
import requests
import pandas
import logging as log
import csv
import time

url = "https://tradecompetitivenessmap.intracen.org/TPIC.aspx"
sectors = ["%.2d" % i for i in range(1, 15)]
headers = ['N', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'P1', 'P2', 'P3', 'P4a', 'P4b',
           'P5a', 'P5b', 'C1', 'C1a', 'C1b', 'C1c', 'C1d', 'C2', 'A', 'P', 'C']


def get_country_number_map_from_file():
    return {row[0]: row[1] for row in csv.reader(open('country-number.csv'))}


country_number_map = get_country_number_map_from_file()


def to_list(sector_values):
    rows = sector_values.find("table", {"id": "RadGrid1_ctl01"}).tbody.findAll("tr")
    if len(rows[0].findAll("td")) < 4:
        log.info("The sector is NOT presented, returning default values...")
        return [[' '] * len(rows)] * 2
    sector_values = [row.findAll("td")[3].text for row in rows]
    sector_ranks = [row.findAll("td")[4].text for row in rows]
    return [sector_values, sector_ranks]


def get_country_data_frame(country):
    with requests.Session() as session:
        response = session.get(url)
        data = basic_data(BeautifulSoup(response.content, "lxml"))
        values_of_country = []
        for sector in sectors:
            log.info("Parsing sector: %s of %s", sector, country)
            response = session.post(url, build_data(data, sector, country_number_map[country]))
            sector_values = BeautifulSoup(response.content, "lxml")
            values_of_country += to_list(sector_values)
    return pandas.DataFrame(values_of_country, columns=headers)


def build_data(data, sector, country_number, year=2016):
    data['dropReporter'] = country_number
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


def get_country_number_map_from_web():
    with requests.Session() as session:
        response = session.get(url)
        soup = BeautifulSoup(response.content, "lxml")
        country_number = {tag.text: tag['value'] for tag in
                          soup.find("select", {"id": "dropReporter"}).findAll("option")}
    return country_number


def get_list_of_countries():
    with open('sub-saharan africa.csv', 'r') as file:
        return [line.strip() for line in file]


def save_all_countries_info():
    log.info("Process have been started...")
    for number, country in enumerate(get_list_of_countries()[:1]):
        log.info("Country: %s number: %s", country, number + 1)
        get_country_data_frame(country).to_csv("countries/{}.csv".format(country), index=False)
        log.info("Country: %s have been saved.", country)
    log.info("Process have been finished.")


def main():
    start_time = time.time()
    save_all_countries_info()
    log.info("Execution time...%s", time.time() - start_time)


if __name__ == '__main__':
    log.basicConfig(level=log.INFO)
    main()
