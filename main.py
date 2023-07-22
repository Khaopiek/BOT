from binance_api import ws
from arbitrage import find_arbitrage_opportunities

def main():
    # Set the WebSocket's on_message function to process_message
    ws.on_message = find_arbitrage_opportunities

    # Run the WebSocket
    ws.run_forever()

if __name__ == "__main__":
    main()
