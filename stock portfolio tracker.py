# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 160,
    "MSFT": 330
}

portfolio = {}
total_value = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# User input
n = int(input("\nHow many different stocks do you own? "))

for i in range(n):
    stock = input(f"\nEnter stock name {i+1}: ").upper()

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available in tracker!")

# Calculate total investment
print("\n--- Portfolio Summary ---")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value
    print(f"{stock} → {quantity} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value = ${total_value}")

# Save to file
save = input("\nDo you want to save results to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Portfolio Summary\n")
        file.write("-----------------\n")

        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(f"{stock}: {quantity} shares = ${value}\n")

        file.write(f"\nTotal Investment Value = ${total_value}")

    print("Results saved in portfolio.txt")
else:
    print("Results not saved.")
