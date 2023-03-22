# 7-Day-Volume-Scanner-for-Crypto-Tokens-using-Coinmarketcap-API
This repo use the coinmarketcap api to fetch all the crypto tokens from all public blockchains which satisfied a pre-determined 7-day trading volume threshold across all listed exchanges on Coinmarketcap, so that crypto traders can make sure they are only trading the altcoins above the volume threshold, narrowing down the crypto pool which the trader's algo is counting on.

Link to the api: https://coinmarketcap.com/api/documentation/v1/

You can also head directly to the Listings Latest endpoint of coinmarketcap api, to see other info which can fetched using other available parameters, 
such as the volume_24h, volume_30d, percent_change_24h, percent_change_7d, etc.
https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
