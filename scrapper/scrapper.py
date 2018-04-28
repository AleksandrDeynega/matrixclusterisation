from bs4 import BeautifulSoup
import requests

base_url = "https://tradecompetitivenessmap.intracen.org/TPIC.aspx"


def url(country):
    return base_url + "?RP=00{}".format(country)


def main():
    with requests.Session() as session:
        response = session.get(url(8))
        # print(response.content)
        soup = BeautifulSoup(response.content, "lxml")

        data = {'__EVENTTARGET': '',
                '__EVENTARGUMENT': '',
                '__LASTFOCUS': '',
                '__VIEWSTATE': soup.find('input', {'name': '__VIEWSTATE'}).get('value', ''),
                '__VIEWSTATEGENERATOR': soup.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value', ''),
                '__EVENTVALIDATION': soup.find('input', {'name': '__EVENTVALIDATION'}).get('value', ''),
                'TradeComTabs1$RadTabStrip1:': '{"State":{},"TabState":{"TradeComTabs1_RadTabStrip1_tabTPI":{"Selected":true},"TradeComTabs1_RadTabStrip1_tabTPI_tabTPIC":{"Selected":true}}}',
                'dropReporter': '024',
                'dropYear': 2016,
                'lbxSector': '14',
                'btnRedo': 'Redo'}

        response = session.post(base_url, data=data)
        #
        soup = BeautifulSoup(response.content, "lxml")
        print(soup.text)



if __name__ == '__main__':
    main()
