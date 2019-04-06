import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb
from scipy.stats import norm

ticker = input('Input Stock Ticker: ')

data = pd.DataFrame()

data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1')['Adj Close']

log_returns = np.log(1 + data.pct_change())

u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5 * var)		
stdev = log_returns.std()
drift.values
stdev.values

x = np.random.rand(10, 2)	
norm.ppf(x)
Z = norm.ppf(np.random.rand(10,2))	

t_intervals = 250
iterations = 100
daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))					#obtain the daily returns (e^r)
S0 = data.iloc[-1]
price_list = np.zeros_like(daily_returns)	
price_list[0] = S0		

for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]	


one_year_forecast=price_list[-1]
price_now=price_list[0]
next_day=price_list[1]
forecast_price=str(round(sum(one_year_forecast)/len(one_year_forecast),2))
current_price=str(round(sum(price_now)/len(price_now),2))
next_day_price=str(round(sum(next_day)/len(next_day),2))
bluechxp_profit=((round(sum(next_day)/len(next_day),2)-round(sum(price_now)/len(price_now),2))/round(sum(price_now)/len(price_now),2))*10000
profit_bluechxp=str(round(bluechxp_profit,2))


print(ticker+' Stock Analysis')
print('The current price of '+ticker+ ' is: $'+current_price)
print('The forecasted price for tomorrow is: $'+next_day_price)
print('The forecasted price of '+ticker+ ' in 1 year is: $'+ forecast_price)
print('The projected profit per $10,000 invested in one day is: $'+ profit_bluechxp)

if bluechxp_profit<10:
    print('We suggest that for day trading, you should not purchase this stock')
else:
    print('We suggest that for day trading, you should purchase this stock')

#plt.figure(figsize=(10,6))
#plt.plot(price_list)
#plt.xlabel('Days')
#plt.ylabel('Price')
#plt.show()


