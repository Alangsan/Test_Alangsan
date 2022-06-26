import requests

#API headers for coinmarketcap
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
params1 = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
params2 = {
  'start':'5001',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '33fd2723-baa9-4ff9-815c-ab5232374a1e',
}

#call Binance API
def binance(coin):
    base_url = "https://api.binance.com/api/v3"
    symbol = coin
    url = base_url + f"/avgPrice?symbol={symbol}USDT"
    r = requests.get(url).json()
    if 'code' in r:
        return "error"
    return r["price"]

#call CoinGecko API
def coingecko(coin):
    coin = coin.lower()
    r = requests.get('https://api.coingecko.com/api/v3/coins').json()
    for i in r:
        if i["symbol"] == coin:
            return i["market_data"]["current_price"]["usd"]
    return "error"

#call CoinMarketCap API
def coinmarketcap(coin):
    r = requests.get(url, params=params1, headers=headers).json()
    all_coins = r['data']

    for x in all_coins:
        if coin == x["symbol"]:
            return x["quote"]["USD"]["price"]

    r = requests.get(url, params=params2, headers=headers).json()
    all_coins = r['data']

    for x in all_coins:
        if coin == x["symbol"]:
            return x["quote"]["USD"]["price"]
    return "error"

#call Kraken API
def kraken(coin):
    r = requests.get(f"https://api.kraken.com/0/public/Ticker?pair={coin}USD").json()
    if r["error"] != []:
        return "error"
    name = list(r["result"])[0]
    return r["result"][name]["a"][0]

##call Okex API
def okx(coin):
    r = requests.get(f"https://www.okex.com/api/v5/market/index-components?index={coin}-USD").json()
    if r["code"] == '0':
        for i in r["data"]["components"]:
            if i["symbol"] == f"{coin}/USD":
                return i["symPx"]
        else:
            return "error"
    else:
        return "error"


