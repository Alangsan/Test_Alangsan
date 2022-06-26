import requests
import statistics
import wrapper

input_ = ["BTC", "ETH", "USDT", "USDC", "BNB", "BUSD"]

#check coin available
all_price = []
for x in input_:
    status = []
    price_bn = wrapper.binance(x)      #check binance
    status.append(price_bn)

    price_cg = wrapper.coingecko(x)   #check coingecko
    status.append(price_cg)

    price_cm = wrapper.coinmarketcap(x)   #check coinmarketcap
    status.append(price_cm)

    price_kk = wrapper.kraken(x)         #check kraken
    status.append(price_kk)

    price_ok = wrapper.okx(x)       #check okx
    status.append(price_ok)
    
    if status.count('error') < 3:   #check error 3 out of 5 sources
        for price in status:
            if price != 'error':
                all_price.append(float(price))
                break
if all_price != []:
    print(statistics.median(all_price),"USD")
else:
    print("No data available")
        


