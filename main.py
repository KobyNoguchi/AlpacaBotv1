from alpaca import api
from strategy import calculate_signals
import requests


# Get market data
data = api.get_barset('AAPL', 'day', limit=10).df['AAPL']

# Calculate signals
signals = calculate_signals(data)

# Place trades based on signals
for signal in signals:
    if signal == 'buy':
        api.submit_order(
            symbol='AAPL',
            qty=1,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
    elif signal == 'sell':
        api.submit_order(
            symbol='AAPL',
            qty=1,
            side='sell',
            type='market',
            time_in_force='gtc'
        )



"""
def createMarketOrder():
    data = {
        'symbol': '',
        'qty': '',
        'side': '',
        'type': '',
        'time_in_force'
    }






"""