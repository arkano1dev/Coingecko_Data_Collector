import requests
import csv
import time

# Get the list of cryptocurrencies
url = 'https://api.coingecko.com/api/v3/coins/markets'
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': '100'
}
response = requests.get(url, params=params)
if response.status_code == 200:
    coin_list = response.json()
    print(coin_list)
else:
    print('An error occurred while making the request.')
    print(response.status_code)

# Write the list of cryptocurrencies with current data to a CSV file
with open('coin_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['market_cap_rank', 'id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume', 'high_24h', 'low_24h', 'price_change_percentage_24h', 'circulating_supply', 'total_supply', 'max_supply']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for i, coin in enumerate(coin_list):
        # Write the current data to a row in the CSV file
        writer.writerow({
            'market_cap_rank': coin['market_cap_rank'],
            'id': coin['id'], 
            'symbol': coin['symbol'], 
            'name': coin['name'], 
            'current_price': coin['current_price'], 
            'market_cap': coin['market_cap'], 
            'total_volume': coin['total_volume'], 
            'high_24h': coin['high_24h'], 
            'low_24h': coin['low_24h'], 
            'price_change_percentage_24h': coin['price_change_percentage_24h'], 
            'circulating_supply': coin['circulating_supply'], 
            'total_supply': coin['total_supply'], 
            'max_supply': coin['max_supply']
        })
        
        # Pause for 1 second before making the next request
        time.sleep(0)

print('Done!')
