# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 150,
    "MSFT": 300
}

total_investment = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

n = int(input("\nHow many stocks do you want to enter? "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_investment)

# Optional: Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Result saved in portfolio.txt")
