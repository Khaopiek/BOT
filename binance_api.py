import websocket
import json
import threading
import time
from keys import API_KEY, API_SECRET

# Binance API rate limits
REQUEST_WEIGHT_PER_MINUTE = 1200
ORDERS_PER_10_SECONDS = 50
ORDERS_PER_24_HOURS = 160000

def on_open(ws):
    print('opened connection')

    # subscribe to depth updates
    subscribe_message = {
        "method": "SUBSCRIBE",
        "params": [f"{currency.lower()}@depth" for currency in selected_currencies],
        "id": 1
    }

    ws.send(json.dumps(subscribe_message))

def on_message(ws, message):
    print('received a message')
    print(message)

def on_close(ws):
    print('closed connection')

def on_error(ws, error):
    print('error occurred')
    print(error)

def run_websocket():
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/stream", 
                                on_open=on_open, 
                                on_message=on_message, 
                                on_close=on_close,
                                on_error=on_error)

    while True:
        try:
            ws.run_forever()
        except Exception as e:
            print(f"Exception: {e}")
            time.sleep(10)  # wait before trying to reconnect

selected_currencies = ['ADATUSD', 'ARBTUSD', 'ARKMTUSD', 'AVAXTUSD', 'BCHTUSD', 'BNBTUSD', 'BTCTUSD', 'CFXTUSD', 'COMPTUSD', 'DOGETUSD', 'EDUTUSD', 'ETHTUSD', 'FLOKITUSD']

# Run the WebSocket in a separate thread
ws_thread = threading.Thread(target=run_websocket)
ws_thread.start()
