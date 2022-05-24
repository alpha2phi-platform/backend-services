import os
import sys
import time
import unittest
import unittest.mock

# Set the library path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from alphalib.data_sources import (get_stock_countries, get_stock_dividends,
                                   get_stock_info, get_stocks,
                                   sanitized_column_name)
from alphalib.models import Stock
from alphalib.utils import get_current_time_utc, logger, parse_datetime


class TestAlphalib(unittest.TestCase):
    """Test out the alphalib library

    - EPS
    - P/E
    - PEG
    - FCF
    - P/B
    - ROE
    - DPR
    - P/S
    - DYR
    - DE

    """

    def setUp(self):
        print("\n---------------- Test Start ----------------\n")

    def tearDown(self):
        print("\n---------------- Test End ----------------\n")

    @unittest.skip("Skipped")
    def test_logger(self):
        logger.info("test_logger")

    @unittest.skip("Skipped")
    def test_set_ts_iso8601(self):
        start = get_current_time_utc()
        time.sleep(1)
        end = get_current_time_utc()
        print(start, end)
        dt_start = parse_datetime(start)
        dt_end = parse_datetime(end)
        dt_diff = dt_end - dt_start
        days_diff = round(dt_diff.total_seconds() / 60 / 24)
        print(days_diff)

    @unittest.skip("Skipped")
    def test_get_stock_countries(self):
        logger.info(get_stock_countries())

    @unittest.skip("Skipped")
    def test_get_stocks(self):
        stocks = get_stocks("united states")
        logger.info(stocks.head(10))

    @unittest.skip("Skipped")
    def test_get_stock_info(self):
        stocks = get_stock_info("AAPL", "united states")
        column_names = stocks.columns.to_list()
        new_column_names = []
        for name in column_names:
            new_column_names.append(sanitized_column_name(name))
        stocks.columns = new_column_names
        logger.info(stocks.head(10))

        # for _, row in stocks.iterrows():
        #     logger.info(json.loads(row.to_json()))

    @unittest.skip("Skipped")
    def test_get_stock_dividends(self):
        stocks_dividends = get_stock_dividends("GM", "united states")
        logger.info(stocks_dividends.columns.to_list())
        column_names = stocks_dividends.columns.to_list()
        new_column_names = []
        for name in column_names:
            new_column_names.append(sanitized_column_name(name))
        stocks_dividends.columns = new_column_names
        logger.info(stocks_dividends.head(1))

    @unittest.skip("Skipped")
    def test_sanitize_column_name(self):
        logger.info(sanitized_column_name("123 (a..) P/E-"))

    @unittest.skip("Skipped")
    def test_stock_model(self):
        stock = {
            "info_update_datetime": None,
            "currency": "USD",
            "symbol": "ZVO",
            "full_name": "Zovio Inc",
            "name": "Zovio",
            "country": "united states",
            "isin": "US98979V1026",
            "inserted_datetime": "2022-05-22T12:47:55+00:00",
        }
        model = Stock(**stock)
        print(model)
        self.assertIsNotNone(model.name)
