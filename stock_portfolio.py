stock_prices = {
    "code": 180,
    "alpha": 250,
    "micro": 200,
    "tcs": 220,
    "info": 210
}

portfolio = {}

print("📈 Welcome to Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or type 'done' to finish): ").lower()
    if stock == 'done':
        break
    elif stock not in stock_prices:
        print("❌ Stock not in list. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity < 0:
            print("❗ Quantity can't be negative.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❗ Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\n🧾 Your Investment Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock}: {qty} shares × ₹{price} = ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_value}")
