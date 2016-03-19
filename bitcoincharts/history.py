# based on
# https://github.com/cnocito/bigdatabitcoinlinkedin/blob/36aefc5a8a1f313eba787c835fcf7d68d19a06cc/downloadalldata.py

from pandas import read_csv
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'http://api.bitcoincharts.com/v1/csv/'
EXTENSION = '.csv.gz'

COLNAMES = ['timestamp', 'price', 'quantity']
DTYPES = ['int', 'float', 'float']


def list_symbols():
    req = urllib.request.urlopen(BASE_URL)
    soup = BeautifulSoup(req.read(), "html.parser")

    links = soup.find_all('a')[1:]
    symbols = [link.text.rstrip(EXTENSION) for link in links]

    return symbols


def download_archive(symbol):
    url = _construct_download_url(symbol)
    content = _read_csv(url)
    return content


def _read_csv(path):
    return read_csv(path,
                    compression='gzip',
                    names=COLNAMES,
                    dtype=dict(zip(COLNAMES, DTYPES)))


def _construct_download_url(symbol):
    return BASE_URL + symbol + EXTENSION
