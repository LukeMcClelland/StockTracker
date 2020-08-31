import pandas as pd  # PANDAS allows to pull data from sources like Yahoo Finance
import numpy as np  # Popular data analytics library
import datetime  # Allows calls for specific periods of time
from datetime import date
from pandas_datareader import data as pdr
import yfinance as yf
from xlwings import Range, Sheet
import matplotlib.pyplot as plt

# Create needed variables
start_sp = datetime.datetime(2020, 4, 8)  # create start and end date variables for desired data pull
end_sp = datetime.datetime(2020, 8, 30)

end_of_year = datetime.datetime(2019, 12, 29)  # used for YTD data

yf.pdr_override()
sp500 = pdr.get_data_yahoo('^GSPC',     # syntax to pull stock data for desired time period
                           start_sp,
                           end_sp)

sp500.head()

# create desired list of stocks
stock_list = ['FB', 'AAPL', 'SPY', 'SMH', 'MSFT', 'BABA', 'VOO', 'QQQ', 'AMZN', 'NVDA', 'VTI', 'ATVI']
number = '12'

stock_data = yf.download(stock_list, start_sp, end_sp, group_by="ticker")
df_data = pd.DataFrame(stock_data)
print(df_data)
writer = pd.ExcelWriter('stockData.xlsx')
df_data.to_excel(writer, sheet_name="1")
writer.save()


