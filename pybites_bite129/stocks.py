import requests
from collections import Counter

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0.0
    if cap[-1] == 'M':
        return float(cap[1:-1])
    if cap[-1] == 'B':
        return float(cap[1:-1])*1000.00



def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    sum_cap = 0
    for stock in data:
        if stock['industry'] == industry:
            # convert to 0 cents to avoid float rounding problem
            sum_cap = sum_cap + _cap_str_to_mln_float(stock['cap'])*100 
    return sum_cap/100


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    return max(data, key=lambda x:_cap_str_to_mln_float(x['cap']))['symbol']


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sectors = [ 
        stock['sector']
        for stock in data 
        if stock['sector'] != 'n/a'
    ]
    counts = Counter(sectors).most_common()
    return counts[0][0], counts[-1][0]