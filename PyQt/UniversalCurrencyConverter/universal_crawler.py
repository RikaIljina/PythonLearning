import requests
import os
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time
import csv


class Crawler:
    def __init__(self):
        self.url_template = 'https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/' \
                            'html/'
        self.base = 'https://sdw.ecb.europa.eu/curConverter.do?sourceAmount=100.0&sourceCurrency=RUB' \
                    '&targetCurrency=EUR&inputDate=18-05-2019&submitConvert.x=55&submitConvert.y=3'
        # self.chosen_currency = 'sek.xml'
        # self.all_rates = []
        # self.last_rate = 0

        # website to crawl for daily rates
        self.daily = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml?b4ec694053eb4cd92b7cbc7345129c0e'

        self.currency_set = set()

        # tuples with (currency abbreviation, rate)
        self.currency_list = []
        self.last_date = ''
        self.xml_content = ''

    def return_options(self):
        try:
            self.get_daily()
            return [entry[0] for entry in self.currency_list]
        except:
            print('error getting rates (in get_daily())')
            return []

    def return_date(self):
        return self.last_date

    def return_rates(self, idx):
        return self.currency_list[idx][1]

    def get_daily(self):
        data = requests.get(self.daily)
        print(data.status_code)
        xml_file = BeautifulSoup(data.text, 'xml')

        all_cubes = xml_file.find('gesmes:Envelope')
        self.last_date = all_cubes.Cube.Cube['time']

        for e in all_cubes.Cube.Cube.findAll('Cube'):
            self.currency_set.add((e['currency'], e['rate']))

        self.currency_list = sorted(list(self.currency_set))
        print(self.currency_list)
        return



        # for entry in xml_file.findAll('Cube'):
        #     if entry.get('currency'):
        #         print(entry)
        #         self.all_rates.append((entry['currency'], entry['rate']))
        #         self.currency_set.add(entry['currency'])
        #     elif entry.get('time'):
        #         print(entry)
        #         self.last_date = entry['time']


# UNUSED:
#     def get_options(self):
#         # crawl a site with all available currencies and save them in a list with tuples
#         data = requests.get(self.base)
#         print(data.status_code)
#         html_file = BeautifulSoup(data.text, 'html.parser')
#
#         options = html_file.select('option')
#         for opt in options:
#             currency_name = opt.text
#             currency_code = opt.attrs['value']
#             self.currency_set.add((currency_name, currency_code))
#
#         # print(self.currency_set)
#         self.currency_list = sorted(list(self.currency_set))
#         # print(self.currency_list)
#         return self.currency_list

    def run(self):
        self.get_daily()

        # self.get_options()
        # idx = self.select_option()
        # self.crawl_rates(idx)
        # self.get_last_rate()

##### Non-GUI logic
    def select_option(self):
        for el in self.currency_list:
            print(self.currency_list.index(el), ' ', el[0], ' -- ', el[1])
        idx = int(input('Pick one: '))

        return idx
#####

# UNUSED:
#     def crawl_rates(self, idx):
#         print('called with ', idx)
#         self.chosen_currency = self.currency_list[idx][1].lower() + '.xml'
#         url_to_crawl = self.url_template + self.chosen_currency
#         print(url_to_crawl)
#         data = requests.get(url_to_crawl)
#         print(data)
#         self.xml_content = BeautifulSoup(data.text, 'lxml')
#         return
#
# UNUSED:
#     def get_last_rate(self):
#         self.all_rates = self.xml_content.compactdata.dataset.series.findAll('obs')
#         rate_count = len(self.all_rates)
#         self.last_rate = (self.all_rates[rate_count - 1]['obs_value'])
#         self.last_date = (self.all_rates[rate_count - 1]['time_period'])
#
#         return


def main():
    my_crawler = Crawler()
    my_crawler.run()


if __name__ == "__main__":
    main()
