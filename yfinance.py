import yfinance

ticker_symbol = input('Type the ticker symbol: ')
lmt = yfinance.Ticker(ticker_symbol)
hist = lmt.history(period='10d')

print((hist))