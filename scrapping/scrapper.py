from bs4 import BeautifulSoup
import requests
import pandas
import logging as log
import time
from scrapping.constants import index, headers, sectors, url, country_number_map, list_of_countries


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
    return pandas.DataFrame(values_of_country, columns=headers, index=index)


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


def save_all_countries_info():
    log.info("Process have been started...")
    for number, country in enumerate(list_of_countries):
        log.info("Country: %s number: %s", country, number + 1)
        get_country_data_frame(country).to_csv("countries/{}.csv".format(country))
        log.info("Country: %s have been saved.", country)
    log.info("Process have been finished.")


def main():
    start_time = time.time()
    save_all_countries_info()
    log.info("Execution time...%s", time.time() - start_time)


if __name__ == '__main__':
    log.basicConfig(level=log.INFO)
    main()
    # print(get_list_of_countries()[21:])
