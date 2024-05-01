import requests
from prettytable import PrettyTable

# API endpoint
url = 'https://api.coingecko.com/api/v3/simple/price'

# Define the cryptocurrencies to track and their amounts in your portfolio
cryptocurrencies = {
    'bitcoin': 0.5,   # Amount of Bitcoin owned
    'ethereum': 1.0,  # Amount of Ethereum owned
}

# Define the parameters for the API request
params = {
    'ids': ','.join(cryptocurrencies.keys()),
    'vs_currencies': 'usd',
}

# Send a GET request to the API
response = requests.get(url, params=params)
data = response.json()

# Create a PrettyTable to display the data
table = PrettyTable()
table.field_names = ['Cryptocurrency', 'Price (USD)', 'Amount', 'Total Value (USD)']

# Calculate the total value of your portfolio and add rows to the table
total_portfolio_value = 0
for crypto, amount in cryptocurrencies.items():
    price = data[crypto]['usd']
    total_value = price * amount
    total_portfolio_value += total_value
    table.add_row([crypto.capitalize(), f'${price:.2f}', amount, f'${total_value:.2f}'])

# Print the table and total portfolio value
print(table)
print(f'Total Portfolio Value: ${total_portfolio_value:.2f}')
