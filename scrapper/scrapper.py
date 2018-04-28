from bs4 import BeautifulSoup
import requests

base_url = "https://tradecompetitivenessmap.intracen.org/TPIC.aspx"


def url(country):
    return base_url + "?RP=00{}".format(country)


def print_values(soup):
    rows = soup.find("table", {"id": "RadGrid1_ctl01"}).tbody.findAll("tr")
    for row in rows:
        print("{}       {}".format(row.findAll("td")[3].text, row.findAll("td")[4].text))


def main():
    # with requests.Session() as session:
    session = requests.Session()
    response = session.get(base_url)
    # print(response.content)
    soup = BeautifulSoup(response.content, "lxml")

    data = {'__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': soup.find('input', {'name': '__VIEWSTATE'}).get('value', ''),
            '__VIEWSTATEGENERATOR': soup.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value', ''),
            '__EVENTVALIDATION': soup.find('input', {'name': '__EVENTVALIDATION'}).get('value', ''),
            'TradeComTabs1$RadTabStrip1:': '{"State":{},"TabState":{"TradeComTabs1_RadTabStrip1_tabTPI":{"Selected":true},"TradeComTabs1_RadTabStrip1_tabTPI_tabTPIC":{"Selected":true}}}',
            'dropReporter': '076',
            'dropYear': 2016,
            'lbxSector': '01',
            'btnRedo': 'Redo'}

    response = session.post(base_url, data=data)
    soup = BeautifulSoup(response.content, "lxml")

    print_values(soup)


if __name__ == '__main__':
    main()
