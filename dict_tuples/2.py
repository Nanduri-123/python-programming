stocks = {'info':[600,630,620],'ril':[1430,1490,1595],'mtl':[234,180,160]}

def print_stocks():
    for stock,prices in stocks.items():
        avg_price = sum(prices) / len(prices)
        print(f"{stocks} ==> {prices} ==> avg : {avg_price:.2f}")

def add_stock(ticker,price):
    if ticker in stocks:
        stocks[ticker].append(price)
    else:
        stocks[ticker] = [price]

def main():
    while True:
        operation = input("Enter 'print' to display stocks or 'add' to add a stock (or 'exit' to quit):").strip().lower()
    
        if operation == 'print':
            print_stocks()
        elif operation == 'add':
            ticker = input("Enter stock ticker:").strip()
            price = float(input("Enter stock price"))
            add_stock(ticker,price)
        elif operation == 'exit':
            break
        else:
            print('Invalid operation. Please try again.')
            

