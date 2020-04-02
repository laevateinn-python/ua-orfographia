import requests
from bs4 import BeautifulSoup

class MyParser(object):
    def get_html(self,url):
        response = requests.get(url)
        return response

    def parse_word_vidminok(self,html):
        soup = BeautifulSoup(html.text)
        table = soup.find('table', class_='main-table1')
        tbody = table.find('tbody').find_all("tr")
        n = []
        for i in range(len(tbody)):
            l = []
            for j in range(len(tbody[i])):
                l.append(tbody[i].find_all('td')[j].text)
            n.append(l)
        return n
    def parse_word_data(self,html):
        soup = BeautifulSoup(html.text)
        word_data = soup.find('section', {'class': 'section section-center orfo'}).text.split(',')
        return word_data
