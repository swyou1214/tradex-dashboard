import pandas as pd
import yfinance as yf

def RSI_Calculator(stock, period = 14):
    stock_data = yf.download(str(stock)) 
    
    if stock_data.empty:
        print("The Stock " + str(stock) + "Doesn't Exist!")
        return
        
    else:
        close_pos = stock_data.tail(period+1) 
        close_pos = close_pos["Close"] #Takes only closing position of stock
    
        diff = close_pos.diff()
        gain = diff.clip(lower=0)
        avg_gain = gain.mean()    
    
        loss = diff.clip(upper=0)
        avg_loss = -loss.mean()

        RS = avg_gain/avg_loss #Relative Strength
        RSI = 100 - (100/(1+RS))
        
        return RSI.item()

def MACD_Calculator():
    return    #WIP


TSLA = RSI_Calculator("TSLA", 14)
NVDA = RSI_Calculator("NVDA", 14)
print(TSLA)
print(NVDA)