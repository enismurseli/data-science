# data-science

# Arkitektura e aplikacionit
  - Aplikacioni do te zhvillohet duke perdorur docker. Mjafton te shkarkohet projekti nga github dhe te behet run komanda 
  `docker-compose up`
  - Ne fajllin docker-compose jane instruksionet ku mund te percaktohet se me cfare korniza do te punohet psh
    - django, celery, PostgreSQL
     
  ...
  - Nxjerrja e te dhenat duhet te behet nga librarite ne python siq jane  yfinance, alpha_vantage, quandl, ccxt, yfinance, ib_insync, yahooquery, pandas_market_calendars


yfinance
```python
import yfinance as yf
ticker = yf.Ticker('AAPL')
df = ticker.history(period='1d', interval='15m')
print(df.head())
```

alpha_vantage
```python
from alpha_vantage.timeseries import TimeSeries
api_key = 'YOUR_API_KEY'
ts = TimeSeries(key=api_key)
data, meta_data = ts.get_intraday(symbol='AAPL', interval='15min', outputsize='full')
print(data.head())
```



quandl
```python
import ccxt
exchange = ccxt.binance()
symbol = 'BTC/USDT'
ohlcv = exchange.fetch_ohlcv(symbol, timeframe='15m', limit=10)
print(ohlcv)
```




# Nxjerrja e te dhenave

- Jane disa instrumente te cilat i percjellim per investime. Qellimi eshte krijimi e nje databaze ku do ti ruajm te dhenat siq jane 
  qmimi ne formatin (OHLC open, high, low, close) dhe paraqitja grafike permes nje aplikacioni te shjesht ne django. 

- Pasi te zhvillohet pjesa per nxjerrjen e te dhenave duhet te krijojm disa celery tasks te cilat e perditesojne databazen e te dhenave

- Se fundi eshte pjesa Data Scraping e cila ka qellim lidhjen e cmimit ne kohe te caktuar me ndonje lajm ne lidhje me ate idnex

- Companies
    Apple Inc. (AAPL) 
    Microsoft Corporation (MSFT) 
    Amazon.com Inc. (AMZN) 
    Alphabet Inc. (GOOGL/GOOG) 
    Johnson & Johnson (JNJ) 
    Procter & Gamble Company (PG) 
    The Coca-Cola Company (KO) 
    Walt Disney Company (DIS) 
    JPMorgan Chase & Co. (JPM) 
    Tesla Inc. (TSLA) 
- Equity Indexes:
    S&P 500 Index (US)
    Dow Jones Industrial Average (US)
    NASDAQ Composite (US)
    FTSE 100 Index (UK)
    DAX Index (Germany)
    Nikkei 225 Index (Japan)
- Currency Pairs (Forex):
    EUR/USD (Euro/US Dollar)
    USD/JPY (US Dollar/Japanese Yen)
    GBP/USD (British Pound/US Dollar)
    USD/CHF (US Dollar/Swiss Franc)
    AUD/USD (Australian Dollar/US Dollar)
- Commodity Indexes:
    S&P GSCI (Commodity Index)
    Bloomberg Commodity Index
    Dow Jones Commodity Index


# Tasks
1.  Store such data on different on Casandra, Mongodb, Redis 
2.  Build a celery tasks that import new data every 8 hours 
3.  Make possible to retrive such data and show them using django 
