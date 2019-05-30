import requests
import os
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time
import csv


sek_url = 'https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/' \
          'eurofxref-graph-sek.en.html'
usd_url = 'https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/' \
          'eurofxref-graph-usd.en.html'
output = 'rates_table.csv'
today = datetime.today().strftime('%Y.%m.%d')


def fetch_rates(url):
    # months start at 0, weekends are left out
    now = str(datetime.today().year) + ',' + str(datetime.today().month - 1) + ',' + str(datetime.today().day)
    r = requests.get(url)
    doc = str(BeautifulSoup(r.text, "html.parser"))
    matchstring = '^.*' + now + '.*$'

    match = re.findall(matchstring, doc, re.MULTILINE)
    print(match)

    try:
        rate_eur = float(re.findall('rate: (.*) ', match[0])[0])
        rate_inv = float(re.findall('rate: (.*) ', match[1])[0])
    except:
        return False, False

    print("rate eur: ", rate_eur)
    print("rate inv: ", rate_inv)

    return rate_eur, rate_inv


def create_weekend_line():
    with open(output, 'r', encoding='utf-8', newline='') as f:
        lines = 0
        while f.readline():
            lines += 1
        f.seek(0)
        for i in range(lines-1):
            next(f)
        old_line = f.readline()
        weekend_line = [today] + old_line[old_line.index(';')+1:].strip('\r\n').split(';')

        return weekend_line


def check_for_recent_update():
    with open(output, 'r+', encoding='utf-8', newline='') as f:
        if today in f.read():
            return False
        else:
            return True


def update_csv():

    update_needed = check_for_recent_update()

    if update_needed:

        with open(output, 'a+', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=';', quotechar='"')
            eur_sek, sek_eur = fetch_rates(sek_url)
            time.sleep(1)
            eur_usd, usd_eur = fetch_rates(usd_url)
            if eur_sek:
                writer.writerow([today, str(eur_sek), str(eur_usd), str(sek_eur), str(usd_eur),
                                 str(sek_eur * 100).split('.')[0] + '.' + str(sek_eur * 100).split('.')[1][:2],
                                 str(usd_eur * 100).split('.')[0] + '.' + str(usd_eur * 100).split('.')[1][:2]])
            else:
                print('\nNo new rates on the weekend. Writing rates from previous date.\n')     # TODO: check if weekend or not updated yet
                writer.writerow(create_weekend_line())

        print(f'\nRates written to file {output}\n')

    else:
        print(f'The rates for {today} have already been added to the file.')

    print(output)
    print(os.path.abspath(output))

    return os.path.abspath(output)


def main():
    update_csv()


if __name__ == "__main__":
    main()

