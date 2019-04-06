#%%
#This code can be used to calculate the potential return of a portfolio per annum
#as well as calculating the volatility rate of the portfolio

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

quantity=int(input('Total number of Stocks you wish to purchase: '))
ticker_input=int(input('How many Tickers do you wish to input?: '))

Ticker=[]
x=[]                                                                                    # x is to append weight at line 27

for i in range(ticker_input):
    Ticker.append(input('Enter The Stock Ticker: '))
    x.append(float(input('Enter Quantity: '))/quantity)


stockdata=pd.DataFrame()

for t in Ticker:
    
    stockdata[t]=wb.DataReader(t,data_source='yahoo',start='2009-1-1')['Adj Close']    # To extract data from Yahoo Finance

returns = (stockdata / stockdata.shift(1)) - 1


weights = np.array(x)

annual_returns = returns.mean() * 250
np.dot(annual_returns, weights)
portfolio=str(round(np.dot(annual_returns, weights),4)*100)+'%'

sec_returns = np.log(stockdata / stockdata.shift(1))

pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))
pfolio_risk=str(round(pfolio_var ** 0.5,4)*100)+'%'

print ('The projected annual return of the portfolio is: '+ portfolio)
print ('The portfolio has a volatility rate of: '+pfolio_risk)


dataplot=input('Would you like to view historial graph?:')

if dataplot=='Yes':
    
    (stockdata / stockdata.iloc[0] * 100).plot()
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title('Portfolio Graph')
    plt.show()