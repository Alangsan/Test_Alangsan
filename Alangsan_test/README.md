###Folder design
- I've designed a folder structure as the following below
Alangsan_test
    ├── handler			# Contain the API handlers
    │   └── wrapper.py              # wrapper function to call all API handlers     
    │	
    │   
    ├── test                    # Contains test scripts
    │   └── example.py          # Example script for using the package
    │ 
    │   
    └── README.md

###Informations
- I've wrote 5 functions to call API links from Binance, CoinGecko, CoinMarketCap,
Kraken, and Okex in the file name 'wrapper.py'

- In the 'example.py' file, it has variable name 'input_' which you can insert any 
list of the cryptocurrency symbol. And when you run the program, it will print out 
the median of the corresponding price in USD or an error.

- If I have more time, I will filter out prices that are outliers. In my idea is to
compare all the 5 values and find percentage of the difference. If the percentage of 
the difference is more than 5%, that number must be rejected.
Example [1001, 1005, 560, 989, 1020]
	compare 1001 to 1005 the difference is 0.39%
 	compare 1001 to 560 the difference is 44.05%
	compare 1001 to 989 the difference is 1.19%
	compare 1001 to 1020 the difference is 1.89%
So that's mean 560 must be rejected. But if base number(For this case is 1001) makes
all percentage difference more than 5%, the base number must be rejected instead.

Moreover, I will make the code simpler and also make the process faster.
	

