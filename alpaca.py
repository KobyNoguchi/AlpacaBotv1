import alpaca_trade_api as tradeapi
from config import *

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=BASE_URL) 

#test to see if account info gets printed
account = api.get_account()
print(account)