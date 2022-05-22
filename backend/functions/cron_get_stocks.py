from .alphalib import (COUNTRY, get_stock_countries, get_stocks,
                       update_countries, update_stocks)


def handler(event, context):

    # Get stock countries
    countries = get_stock_countries()
    update_countries(countries)

    # Get stocks
    stocks = get_stocks(COUNTRY)
    update_stocks(stocks)

    return {}
