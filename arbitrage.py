from binance_api import ws  # Import the WebSocket connection from binance_api.py
from collections import defaultdict

FEE = 0.00075
PRIMARY = ['ADATUSD', 'ARBTUSD', 'ARKMTUSD', 'AVAXTUSD', 'BCHTUSD', 'BNBTUSD', 'BTCTUSD', 'CFXTUSD', 'COMPTUSD', 'DOGETUSD', 'EDUTUSD', 'ETHTUSD', 'FLOKITUSD']

def process_message(msg):
    # Extract the bids and asks from the message
    bids = {float(price): float(quantity) for price, quantity in msg['bids']}
    asks = {float(price): float(quantity) for price, quantity in msg['asks']}

    # Store the bids and asks in a dictionary
    order_book = {'bids': bids, 'asks': asks}

    # Find arbitrage opportunities using the order book
    find_arbitrage_opportunities(order_book)

def find_arbitrage_opportunities(order_book):
    # Get the latest prices
    prices = get_prices(order_book)

    # Your code for finding arbitrage opportunities goes here
    # This will depend on your specific strategy

    # For example, you might look for situations where you can trade A -> B -> C -> A for a profit

def get_prices(order_book):
    prepared = defaultdict(dict)

    for primary in PRIMARY:
        for secondary in order_book['asks']:
            if secondary == primary:
                continue

            prepared[primary][secondary] = 1 / order_book['asks'][secondary]

        for secondary in order_book['bids']:
            if secondary == primary:
                continue

            prepared[secondary][primary] = order_book['bids'][secondary]

    return prepared

# Set the WebSocket's on_message function to process_message
ws.on_message = process_message
