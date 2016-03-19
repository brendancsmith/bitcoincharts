import unittest
from unittest.mock import patch, Mock

import os
import pandas as pd

import bitcoincharts.history as history


CONTENT_DIR = 'mock_content/'


class HistoryUnitTest(unittest.TestCase):

    def setUp(self):
        testdir = os.path.dirname(os.path.realpath(__file__))
        self.contentDir = os.path.join(testdir, CONTENT_DIR)

    @patch("bitcoincharts.history.urllib.request")
    def test_list_symbols(self, mock_urllib_request):
        with open(self.contentDir + 'csv_index.html') as f:
            html = f.read()
        mock_urllib_request.urlopen.return_value.read.return_value = html

        with open(self.contentDir + 'symbols.txt') as f:
            expected_symbols = f.read().splitlines()

        result_symbols = history.list_symbols()

        self.assertEqual(expected_symbols, result_symbols)

    @patch("bitcoincharts.history._construct_download_url")
    def test_download_archive(self, mock_construct_download_url):
        mock_construct_download_url.return_value = self.contentDir + 'bcmMBUSD.csv.gz'

        mock_csv = Mock(spec=pd.DataFrame())
        mock_csv.shape = (136, 3)
        mock_csv.columns.values = history.COLNAMES
        mock_csv.dtypes = history.DTYPES

        result_csv = history.download_archive('bcmMBUSD')

        self.assertEqual(mock_csv.shape, result_csv.shape)
        self.assertEqual(mock_csv.columns.values,
                         list(result_csv.columns.values))

        for expected_dt, result_dt in zip(mock_csv.dtypes, result_csv.dtypes):
            self.assertTrue(expected_dt in str(result_dt))

    def test_construct_download_url(self):
        expected = 'http://api.bitcoincharts.com/v1/csv/bcmMBUSD.csv.gz'
        result = history._construct_download_url('bcmMBUSD')
        self.assertEqual(expected, result)
